import os
import moviepy 

def convert_mp4_to_gif():
    try:
        # Get current directory
        current_dir = os.getcwd()
        
        # Find all MP4 files in current directory
        mp4_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.mp4')]
        
        if not mp4_files:
            return "No MP4 files found in the current directory!"
        
        results = []
        
        for mp4_file in mp4_files:
            try:
                # Generate output gif filename (same name, different extension)
                gif_file = os.path.splitext(mp4_file)[0] + '.gif'
                
                # Load video file
                clip = VideoFileClip(mp4_file)
                
                # Calculate new dimensions while maintaining aspect ratio
                # Target width of 480 pixels for good balance of quality and file size
                target_width = 480
                aspect_ratio = clip.w / clip.h
                new_height = int(target_width / aspect_ratio)
                
                # Resize clip
                resized_clip = clip.resize(width=target_width, height=new_height)
                
                # Write to GIF with optimized settings
                resized_clip.write_gif(
                    gif_file,
                    fps=15,              # Reduced FPS for smaller file size
                    program='ffmpeg',    # Using ffmpeg for better performance
                    opt='OptimizePlus', # High quality optimization
                    fuzz=2              # Slight color fuzz for better compression
                )
                
                # Close clips to free memory
                resized_clip.close()
                clip.close()
                
                results.append(f"Successfully converted {mp4_file} to {gif_file}!")
                
            except Exception as e:
                results.append(f"Error converting {mp4_file}: {str(e)}")
                continue
        
        return "\n".join(results)
    
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
