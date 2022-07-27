from collections import namedtuple
from tkinter.font import nametofont
from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
["train_file_path","test_file_path","is_ingested","message"])