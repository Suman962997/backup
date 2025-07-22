import pdfplumber
import pytesseract
from PIL import Image
import io
import re
import time

sec_a_II_1={
    "q_starts": [
    "Details of business activities (accounting for 90% of the turnover)",
    "Details of business activities",
    "accounting for 90% of the turnover",],
    
    "q_ends":[
    "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)",
    "Products/Services sold by the",
    "accounting for 90% of the entity’s Turnover" ],
    
    "keys": [
        "Description of Main Activity",
        "Description of Business Activity",
        "% of Turnover of the entity",],
    "pages":10,
}


print(sec_a_II_1.get("MY"))

