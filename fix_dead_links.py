#!/usr/bin/env python3
"""
Fix dead links in Strategic Communication category
"""
import json
import os

def fix_main_links():
    """Fix links in Main category"""
    filepath = "_data/links/StrategicCommunication/Main/links.json"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filter out BlueWhitePublicity (dead DNS)
    original_count = len(data['links'])
    data['links'] = [link for link in data['links'] if link['name'] != 'BlueWhitePublicity']
    removed_count = original_count - len(data['links'])
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Fixed Main/links.json: Removed {removed_count} dead initiative(s)")
    return removed_count

def fix_social_networks_links():
    """Fix links in Social Networks category"""
    filepath = "_data/links/StrategicCommunication/SocialNetworks/links.json"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changes = []
    removed = []
    
    for link in data['links']:
        # Fix Oct7.App URL
        if link['name'] == 'Oct7.App' and link['url'] == 'https://app.oct7.io/':
            link['url'] = 'https://www.oct7.io/'
            changes.append(f"Oct7.App: Updated URL to https://www.oct7.io/")
        
        # Mark initiatives to remove (completely dead DNS)
        if link['name'] in ['israelfightsback', 'ShareItIl', 'BlockTheHate']:
            removed.append(link['name'])
    
    # Remove dead initiatives
    original_count = len(data['links'])
    data['links'] = [link for link in data['links'] if link['name'] not in removed]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Fixed SocialNetworks/links.json:")
    for change in changes:
        print(f"  - {change}")
    if removed:
        print(f"  - Removed {len(removed)} dead initiative(s): {', '.join(removed)}")
    
    return len(changes) + len(removed)

def main():
    os.chdir('/data/.openclaw/workspace/LinksForIsrael')
    
    print("Fixing dead links in Strategic Communication category...\n")
    
    total_changes = 0
    total_changes += fix_main_links()
    total_changes += fix_social_networks_links()
    
    print(f"\n✓ Total changes: {total_changes}")
    print("\nNote: Kept 'לנצח כל אדיוט בויכוח' (commentron.ai) as it has alternative")
    print("YouTube and LinkedIn links that may still be valid.")

if __name__ == '__main__':
    main()
