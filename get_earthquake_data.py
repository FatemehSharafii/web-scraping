import pandas as pd
import wikipedia as wp


def get_earthquake_data(EQName):
#Get the html source
    html = wp.page(EQName+ " earthquake").html().encode("UTF-8")

    df = pd.read_html(html)[0]
    df=df.set_index([0])
    df=df.loc[["Duration","Magnitude", "Depth", "Type", "Areas affected","Total damage", "Peak acceleration", "Casualties"], 1]
    df.to_excel(EQName+ '.xlsx',header=0,index=["Duration","Magnitude", "Depth", "Type", "Areas affected","Total damage", "Peak acceleration", "Casualties"])
