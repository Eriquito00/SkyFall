import os
import tempfile
from pathlib import Path

import pandas as pd
import numpy as np

class MeteoriteDAO:
    def __init__(
        self,
        file_path: str | Path = "src/persistence/data/meteorite_landings.csv",
        writable_file_path: str | Path | None = None,
    ):
        self.file_path = Path(file_path)
        self.writable_file_path = (
            Path(writable_file_path)
            if writable_file_path is not None
            else self.file_path.with_name(
                f"{self.file_path.stem}_editable{self.file_path.suffix}"
            )
        )
        self.columns = pd.read_csv(self.file_path, nrows=0).columns.tolist()

    def load_all(self) -> list[dict]:
        data_file = (
            self.writable_file_path
            if self.writable_file_path.exists()
            else self.file_path
        )
        df = pd.read_csv(data_file)
        df = df.replace({np.nan: None})
        return df.to_dict(orient="records")

    def save_all(self, meteorites: list[dict]) -> None:
        self.writable_file_path.parent.mkdir(parents=True, exist_ok=True)
        df = pd.DataFrame(meteorites, columns=self.columns)
        with tempfile.NamedTemporaryFile(
            dir=self.writable_file_path.parent,
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)

        try:
            df.to_csv(temporary_path, index=False)
            os.replace(temporary_path, self.writable_file_path)
        finally:
            temporary_path.unlink(missing_ok=True)
