# GitHub Pages 用の公開ファイル（docs/index.html）を作る。
# index.html（Claudeのアーティファクト用）に、単体で全画面表示するための head を足すだけ。
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
body = (root / 'index.html').read_text(encoding='utf-8')
head = '''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Long Range 3D">
<meta name="theme-color" content="#000000">
'''
(root / 'docs').mkdir(exist_ok=True)
(root / 'docs' / 'index.html').write_text(head + body, encoding='utf-8')
(root / 'docs' / '.nojekyll').write_text('', encoding='utf-8')
print('docs/index.html', len(head + body))
