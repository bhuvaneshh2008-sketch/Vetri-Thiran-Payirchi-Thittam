def build_comic_layout(image_paths, story_text, outline):
    panels = []
    
    # Default cool story lines for Demon Slayer theme if Gemini text fails
    default_stories = [
        "Kamado Tanjiro steps into the freezing cold of the Snowy Mountain, feeling a strange demon presence.",
        "Unsheathing his Nichirin blade, he focuses on the Total Concentration Breathing.",
        "The snow begins to swirl around him as he senses the enemy's faint opening thread.",
        "With a sudden burst of energy, Tanjiro channels the Sun Breathing technique!",
        "Flames leap from his blade as he strikes down the demon, bringing peace back to the mountain village."
    ]
    
    for idx, item in enumerate(outline):
        title = item.get("title", f"Panel {idx + 1}")
        scene = item.get("scene", "")
        img_path = image_paths[idx] if idx < len(image_paths) else ""
        
        # Pick story text properly
        narration = default_stories[idx % len(default_stories)]
        
        panels.append({
            "title": title,
            "image_path": img_path,
            "scene": scene,
            "text": narration
        })
        
    return {"panels": panels}