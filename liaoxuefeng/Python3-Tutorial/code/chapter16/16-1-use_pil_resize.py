#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

# ��һ��jpgͼ���ļ���ע���ǵ�ǰ·��:
im = Image.open('test.jpg')
# ���ͼ��ߴ�:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# ���ŵ�50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# �����ź��ͼ����jpeg��ʽ����:
im.save('thumbnail.jpg', 'jpeg')