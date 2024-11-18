import os
from abc import ABC
import boto3
from botocore.exceptions import NoCredentialsError
from PIL import Image
import io
import fitz
import requests
import io
from pypdf import PdfReader, PdfWriter


class File(ABC):
    @staticmethod
    def create_pdf(name:str):
        print("created file successfully...")