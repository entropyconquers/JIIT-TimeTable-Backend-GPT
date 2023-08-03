#load OPENAI_API_KEY from .env file
from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hello World')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
