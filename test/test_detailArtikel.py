from helper.action import *
from helper.config import *
from pom.POM_detail import *
from pom.POM_home import *

def test_detail_scope_share(openDriver):
    element_click(openDriver, titleNews)
    validasi_url(openDriver, detailArtikelNews)
    element_click(openDriver, waShare)
    element_click(openDriver, fbShare)
    element_click(openDriver, xShare)
    element_click(openDriver, lineShare)
    element_click(openDriver, gmailShare)
    element_click(openDriver, copyLinkShare)

def test_detail_scope_nav(openDriver):
    element_click(openDriver, titleNews)
    validasi_url(openDriver, detailArtikelNews)
    element_click(openDriver, articleNav1)
    element_click(openDriver, articleNav2)
    element_click(openDriver, articleNav3)
    element_click(openDriver, articleNav4)

def test_hide_open_nav(openDriver):
    element_click(openDriver, titleNews)
    validasi_url(openDriver, detailArtikelNews)
    validate_is_display(openDriver, hideNavArticle)
    #element_click(openDriver, hideNavArticle)