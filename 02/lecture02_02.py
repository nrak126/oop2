import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    # ルート要素を作成
    root = ET.Element('book')
    
    # article要素を作成
    article = ET.SubElement(root, 'article', title='卒業論文')
    
    # articleの章を追加
    ET.SubElement(article, 'chapter', id='1', name='はじめに', pages='2')
    ET.SubElement(article, 'chapter', id='2', name='基礎理論', pages='8')
    ET.SubElement(article, 'chapter', id='3', name='実験方法', pages='6')
    ET.SubElement(article, 'chapter', id='4', name='結果と考察', pages='2')
    ET.SubElement(article, 'chapter', id='5', name='まとめ', pages='1')
    ET.SubElement(article, 'chapter', id='6', name='参考文献', pages='2')
    
    # novel要素を作成
    novel = ET.SubElement(root, 'novel')
    
    # novelの章を追加
    ET.SubElement(novel, 'chapter', id='1', name='1日のはじまり', pages='2')
    ET.SubElement(novel, 'chapter', id='2', name='朝食', pages='8')
    ET.SubElement(novel, 'chapter', id='3', name='仕事', pages='6')
    ET.SubElement(novel, 'chapter', id='4', name='帰宅後', pages='2')
    ET.SubElement(novel, 'chapter', id='5', name='新しい朝', pages='1')
    
    # ツリーを作成してファイルに書き出す
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ')
    tree.write('lecture02_02_data.xml', encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    lecture02_02()