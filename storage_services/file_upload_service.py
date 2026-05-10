import uuid
import aiofiles
from pathlib import Path
from fastapi import UploadFile

from constants.file_storage_constant import UPLOAD_DIR, ALLOWED_TYPES, MAX_SIZE_BYTES
from exceptions import UnSupportedFileException, LargeFileException

class FileUploadService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FileUploadService, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.upload_dir = Path(UPLOAD_DIR)
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.allowed_types = ALLOWED_TYPES
        self.max_size = MAX_SIZE_BYTES
    
    def _validate(self, file: UploadFile, contents: bytes) -> None:
        if file.content_type not in self.allowed_types:
            raise UnSupportedFileException()
        if len(contents) > self.max_size:
            raise LargeFileException()

    async def upload(self, file: UploadFile) -> str:
        """Saves the file and returns its URL path."""
        contents = await file.read()
        self._validate(file, contents)

        ext = Path(file.filename).suffix.lower()
        unique_name = f"{uuid.uuid4().hex}{ext}"
        dest = self.upload_dir / unique_name

        async with aiofiles.open(dest, "wb") as f:
            await f.write(contents)

        return f"/uploads/{unique_name}"