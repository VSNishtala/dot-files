#!/usr/bin/env python3

import argparse
import pathlib
import random

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def random_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    h = int(360.0 * 143.0 / 255.0)
    s = int(77.0 * 255.0 / 255.0)
    l = int(100.0 * float(random.randint(44, 100)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--filename", "-f", dest="filename", required=True, help="Markdown/text file"
    )
    parser.add_argument(
        "--save_dir",
        "-s",
        dest="save_location",
        required=True,
        help="Location to save the image.",
    )

    args = vars(parser.parse_args())

    with open(args.get("filename")) as _f:
        contents = " ".join([i.strip() for i in _f.readlines()])

    if contents:
        wordcloud = WordCloud(
            width=900,
            height=200,
            stopwords=STOPWORDS,
            collocations=False,
            mode="RGB",
            margin=10,
            random_state=4,
            max_words=50,
        ).generate(contents)
        wordcloud.recolor(color_func=random_color_func)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        location = pathlib.Path(args.get("save_location")).absolute()
        plt.savefig(location, bbox_inches="tight", dpi=300)


if __name__ == "__main__":
    main()
