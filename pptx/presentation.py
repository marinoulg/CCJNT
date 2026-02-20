from pptx import Presentation
from pptx.util import Inches
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

import os
import pandas as pd
from datetime import date

from method.params import *
from method.methode_ecologiedatagouvfr import possibilities

def title_page(ppt, title, heading, subheading):
    page = ppt.slides.add_slide(title)
    page.shapes.title.text = heading
    page.placeholders[1].text = subheading

def content_page(ppt,
                 content,
                 slide,
                 page,
                 heading=None,
                 img=None,
                 subheading_df=None):

    # Split heading into max 2 lines
    if heading:
        if len(heading) > 50:
            middle = len(heading)//2
            space = heading.find(" ", middle)
            heading_line1 = heading[:space]
            heading_line2 = heading[space + 1:]

            page.shapes.title.text = f"{heading_line1}\n{heading_line2}"
        else:
            page.shapes.title.text = heading

    # Optionally, set a smaller font size for the title to ensure it fits
    for paragraph in page.shapes.title.text_frame.paragraphs:
        paragraph.font.size = Pt(24)  # Adjust font size as needed

    if subheading_df is not None and not subheading_df.empty:
        if slide == 1:
            left = Inches(0.5)
        else:
            left = Inches(4.7)
        # Add a table to the slide
        rows, cols = subheading_df.shape
        top = Inches(1.5)
        width = Inches(8)
        height = Inches(0.5 * rows)  # Adjust height based on number of rows

        table = page.shapes.add_table(rows + 1, cols, left, top, width, height).table

        # Function to set cell text with uniform font size and word wrap
        def set_cell_text(cell, text):
            tf = cell.text_frame
            tf.word_wrap = True
            tf.clear()  # Clear existing paragraphs
            p = tf.add_paragraph()
            p.text = str(text)
            p.font.size = Pt(8)  # Set small font size for all text
            p.alignment = PP_ALIGN.LEFT

        # Add header (column names)
        for col_idx, column in enumerate(subheading_df.columns):
            set_cell_text(table.cell(0, col_idx), str(column))

        # Add data
        for row_idx in range(rows):
            for col_idx in range(cols):
                set_cell_text(table.cell(row_idx + 1, col_idx), str(subheading_df.iat[row_idx, col_idx]))

        # Set column widths: first column narrow, second column wide
        if cols == 2:
            table.columns[0].width = Inches(1)  # First column: 1 inch wide
            table.columns[1].width = Inches(4)  # Second column: 7 inches wide
        elif cols > 2:
            table.columns[0].width = Inches(1)  # First column: 1 inch wide
            table.columns[1].width = Inches(1)  # Second column: 7 inches wide
            table.columns[2].width = Inches(7)  # Second column: 7 inches wide


    if img:
        left = Inches(0.2)
        top = Inches(1.7)
        # width = Inches(6)
        height = Inches(5)
        page.shapes.add_picture(img, left, top, height=height)

def get_1_img(img_png_name, elem, OUTPUTS_TERRITORY):
    img_title = img_png_name.replace(".png","")
    img_path = os.path.join(OUTPUTS_TERRITORY, elem, img_png_name)
    return img_path, img_title


# ------- helper functions to create table of information ----
def find_elem_in_INFORMATIONS(tofind):

    df = pd.DataFrame()
    for elem in INFORMATIONS:
        if tofind in elem:
            df_new = pd.DataFrame([elem, INFORMATIONS[elem]])
            df = pd.concat([df, df_new], axis=1)

    df = df.T.rename(columns={0:"Nom de colonne", 1:"Description"})
    return df

def create_df_for_information(merged, possibilities):
    to_show = set()
    for possibility in possibilities:
        for cat_index in merged.index.tolist():
            if possibility in cat_index:
                to_show.add(possibility)
    to_show = list(to_show)

    df = pd.DataFrame()
    for elem in to_show:
        if df.columns.tolist() == []:
            df = find_elem_in_INFORMATIONS(elem)
        else:
            df_new = pd.DataFrame(find_elem_in_INFORMATIONS(elem))
            df = pd.concat([df, df_new], axis=0)
    return df


if __name__ == "__main__":
    ppt = Presentation()
    title = ppt.slide_layouts[0]
    content = ppt.slide_layouts[1]

    quelle_commune = os.path.join(LOCAL_PATH_OUTPUTS,"valenciennes")

    heading = quelle_commune.split("/")[-1].replace("_", " ").title()
    title_page(ppt, title, heading, f"created by Marine on {date.today()}\n for Cerema - CCJNT")

    df = pd.read_csv(os.path.join(LOCAL_DATA_PATH,"demarches_entetes_V2.csv"), sep=";", header=None).iloc[1:,1:].dropna(axis=0, how="all")
    for num_col, title_col in zip(df.columns.tolist(), df.iloc[0,:].values.tolist()):
        df.rename(columns={num_col:title_col}, inplace=True)
    df = df.drop(index=2).reset_index().drop(columns=["index"])

    content_page(ppt,
                 slide=1,
                 content=content,
                 page= ppt.slides.add_slide(content),
                 heading="General information",
                 subheading_df=df)
    slide = 2
    for directory in os.listdir(os.path.join(LOCAL_PATH_REPO, "outputs", quelle_commune)):
        print(directory)
        page = ppt.slides.add_slide(content)
        for file in os.listdir(os.path.join(LOCAL_PATH_REPO, "outputs", quelle_commune, directory)):
            print(file)
            img_path, img_title = None, None
            tmp_df = None

            if file.endswith(".png"):
                img_path, img_title = get_1_img(img_png_name=file, elem=directory, OUTPUTS_TERRITORY=quelle_commune)
                print("img:", slide)
                content_page(ppt,
                            content,
                            page=page,
                            slide=slide,
                            img=img_path,
                            heading=img_title,
                            # subheading_df=tmp_df
                            )

            if file.endswith(".csv"):
                merged = pd.read_csv(os.path.join(quelle_commune, directory, file), sep=";").set_index("Categories")
                tmp_df = create_df_for_information(merged, possibilities)
                print("csv:", slide)
                print(os.listdir(os.path.join(quelle_commune, directory)))
                content_page(ppt,
                            content,
                            page=page,
                            slide=slide,
                            # img=img_path,
                            heading=[img_title if img_path is not None else directory][0],
                            subheading_df=tmp_df,
                            )
                """
                Quand on parle de "Diagnostic" dans merged,
                dire de quand date le diagnostic en le rajoutant
                en format subtext
                """
        slide += 1  # Increment slide only once per file
        print()

    path_created = os.path.join(LOCAL_PATH_REPO,"pptx",quelle_commune)
    print("path: ",path_created)

    os.makedirs(path_created, exist_ok=True)
    ppt.save(os.path.join(path_created, f"{heading}.pptx"))

    print("Complete")
