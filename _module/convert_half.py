# 全角の文字列を半角文字列に変換する関数
def conv_half(before):

    # 全角の文字列
    FULLWIDTH_DIGITS = "０１２３４５６７８９"
    FULLWIDTH_ALPHABET = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    FULLWIDTH_PUNCTUATION = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～　"
    FULLWIDTH_ALPHANUMERIC = FULLWIDTH_DIGITS + FULLWIDTH_ALPHABET  # 英数字
    FULLWIDTH_ALL = FULLWIDTH_ALPHANUMERIC + FULLWIDTH_PUNCTUATION  # 英数字、記号

    # 半角の文字列
    HALFWIDTH_DIGITS = "0123456789"
    HALFWIDTH_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    HALFWIDTH_PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
    HALFWIDTH_ALPHANUMERIC = HALFWIDTH_DIGITS + HALFWIDTH_ALPHABET  # 英数字
    HALFWIDTH_ALL = HALFWIDTH_ALPHANUMERIC + HALFWIDTH_PUNCTUATION  # 英数字、記号

    conv_map = str.maketrans(FULLWIDTH_ALL, HALFWIDTH_ALL)

    after = before.translate(conv_map)

    return after