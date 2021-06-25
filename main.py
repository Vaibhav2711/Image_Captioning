from caption import image_cap

cap = image_cap('img/objects.jpeg','../BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar','../WORDMAP_coco_5_cap_per_img_5_min_word_freq.json',5)
print(cap)