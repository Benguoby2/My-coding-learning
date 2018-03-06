# 廖雪峰 python学习
"""
生成字母验证码
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
	return chr(random.randint(64, 90))

# 随机颜色
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def randColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB, (width, height), (255,255,255))
# 创建Font对象
font = ImageFont.truetypr('C:\Windows\Fonts\Arial.ttf', 36)

#  创建Draw对象
draw = ImageDraw。Draw（image）
for x in range(width):
	for y in range(height)；
		draw.point((x, y), fill=rndcolor())
for t in range(4):
	draw.text((60*t+10,10), rndChar(), font=font, fill=rndColor2())

image.save('code.jpg', 'jpeg')
