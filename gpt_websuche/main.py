import pandas as pd
from chatGPT import get_gpt_answer

EXCEL_DATEI = "Städte.xlsx"

df = pd.read_excel(EXCEL_DATEI, dtype=str)

def finde_buergermeister():
    for i, zeile in df.iterrows():
        stadt = zeile["Stadt"]
        prompt = f"Es geht um die Stadt {stadt}. Suche nach dem aktuellen Bürgermeister. Antworte nur mit dem Vor-und Nachnamen."
        buergermeister = get_gpt_answer(prompt)
        
        print(f"Schreibe {buergermeister} für {stadt}.")
        df.at[i, "Bürgermeister"] = buergermeister
        
if __name__ == "__main__":
    finde_buergermeister()
    df.to_excel("Städte_fertig.xlsx")
        