class BookLocators:
    NAME = 'article.product_pod h3 a'
    LINK = 'article.product_pod h3 a'
    PRICE = 'article.product_pod p.price_color'
    RATING = 'article.product_pod p.star-rating'

    """ NOTE: Dont't always need the full path, as long as the elements are nested inside the previous
    e.g. article div.product_price p.price_color can be shortened as the p.price_color is nested inside the article tag
    """