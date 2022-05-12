import requests
from gooey import Gooey, GooeyParser
import pandas as pd

# mac colors (sigh) footer_bg_color="#789CA4", sidebar_bg_color="#789CA4", body_bg_color="#789CA4", header_bg_color="#789CA4"
@Gooey(program_name="PhoneData", program_description="Find info on phone numbers.")
def get_args():
    f = open("country_codes.html")
    dfs = pd.read_html(f)
    df = dfs[0]  # pd.read_html reads in all tables and returns a list of DataFrames
    summary = {k: v.iloc[0, 1] for k, v in df.groupby(0)}
    parser = GooeyParser()
    parser.add_argument("-n", "--Number", type=str, nargs="+", required=True)
    parser.add_argument("-l", "--Location", widget="FilterableDropdown", choices=summary, required=True)
    args = parser.parse_args()
    phone_num = args.Number
    country = args.Location
    code = summary.get(country)
    return phone_num, code

def main(num, country_code):
    
    url = f"https://api.apilayer.com/number_verification/validate?number={country_code+''.join(num)}"

    payload = {}
    headers= {
        "apikey": "G72bv4bDfUZ9wlmVZdxSZY9ejOfQg7QX"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    return result

if __name__ == '__main__':
    raise SystemExit(print(main(*get_args())))