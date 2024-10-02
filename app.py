import os
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from sklearn.cluster import KMeans

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            images.append(Image.open(img_path).convert("RGB"))
    return images

def create_gradient(size, color1, color2):
    gradient = Image.new('RGB', size)
    for y in range(size[1]):
        r = int(color1[0] * (1 - y / size[1]) + color2[0] * (y / size[1]))
        g = int(color1[1] * (1 - y / size[1]) + color2[1] * (y / size[1]))
        b = int(color1[2] * (1 - y / size[1]) + color2[2] * (y / size[1]))
        for x in range(size[0]):
            gradient.putpixel((x, y), (r, g, b))
    return gradient

def extract_dominant_colors(image, num_colors=2):
    image = image.resize((100, 100))
    image_array = np.array(image)
    pixels = image_array.reshape(-1, 3)
    
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_.astype(int)
    return [tuple(color) for color in colors]

def apply_theme(image, text, colors, theme):
    draw = ImageDraw.Draw(image.copy())
    font = ImageFont.load_default()
    
    text_position = (10, 10)
    text_color = colors[0]  # Use the first dominant color for text
    draw.text(text_position, text, fill=text_color, font=font)
    
    return image

def create_banners(num_images, promotional_offers, themes):
    banners = []
    
    for _ in range(num_images):
        selected_image = random.choice(image_dataset).copy()
        
        text = random.choice(promotional_offers)
        theme = random.choice(themes)

        # Extract dominant colors from the selected image
        dominant_colors = extract_dominant_colors(selected_image, num_colors=2)

        # Create gradient background using the extracted dominant colors
        gradient_bg = create_gradient(selected_image.size, dominant_colors[0], dominant_colors[1])

        # Combine the gradient background with the selected image
        banner = Image.alpha_composite(gradient_bg.convert('RGBA'), selected_image.convert('RGBA'))
        
        # Apply theme and create banner
        banner = apply_theme(banner, text, dominant_colors, theme)
        banners.append(banner)
    
    return banners

def save_banners(banners, folder="banners"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i, banner in enumerate(banners):
        banner.save(f"{folder}/banner_{i + 1}.png")

# Example usage
image_dataset = load_images_from_folder('untagged')
promotional_offers = ["MAX ₹99 OFF", "UP TO 60% OFF", "UNDER ₹999", "MIN ₹10 OFF", "MIN 20% OFF", "STARTS @₹99", "FLAT ₹100 OFF", "FLAT 20% OFF", "₹499 STORE", "BUY 2 GET 1 FREE"]
themes = ["diwali", "independence_day"]

banners = create_banners(num_images=1, promotional_offers=promotional_offers, themes=themes)
save_banners(banners)