python early in masl_early_saves:
    import os
    import __main__
    import renpy

    saves_dir = __main__.path_to_saves(renpy.config.gamedir)

    if saves_dir and os.path.exists(saves_dir):
        target_per = os.path.join(saves_dir, "persistent_699")
        
        if os.path.exists(target_per):
            cur_per = os.path.join(saves_dir, "persistent")
            old_per = os.path.join(saves_dir, "persistent.old")
            migrated_per = os.path.join(saves_dir, "persistent.migrated")
            
            if os.path.exists(cur_per):
                if os.path.exists(old_per):
                    try:
                        os.remove(old_per)
                    except Exception:
                        pass
                try:
                    os.rename(cur_per, old_per)
                except Exception:
                    pass
            
            if os.path.exists(migrated_per):
                try:
                    os.remove(migrated_per)
                except Exception:
                    pass
            
            if os.path.exists(cur_per):
                try:
                    os.remove(cur_per)
                except Exception:
                    pass
            try:
                os.rename(target_per, cur_per)
            except Exception:
                pass
