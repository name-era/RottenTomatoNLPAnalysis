import pandas as pd
import re
from wordcloud import WordCloud

if __name__ == '__main__':
    papers = pd.read_csv('./call_me_by_your_name.csv')
    papers['paper_text_processed'] = papers['quote'].map(lambda x: re.sub('[,\.!?]', '', x))
    long_string = ','.join(list(papers['quote'].values))
    wordcloud=WordCloud(background_color="White", max_words=5000, contour_width=3,contour_color="steelblue")
    wordcloud.generate(long_string)
    img=wordcloud.to_image()
    img.save("image.png")