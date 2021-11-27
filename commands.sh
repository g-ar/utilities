# These are different commands, not a single shell script

# 1. compress a video, e.g. video recorded from phone. libx265 for more compression
ffmpeg -i input.avi -vcodec libx264 -crf 24 output.avi

# 2. convert all jpg files, and store in a directory
for f in ./*.jpg; do convert -resize 50% $f res/${f%.jpg}_res.jpg ; done;

# 3. enable copy/paste fields in websites; if ctrl-v does not work, try shift-ins
# chrome
var allowPaste = function(e){
  e.stopImmediatePropagation();
  return true;
};
document.addEventListener('paste', allowPaste, true);
# firefox: disable clipboard events in about:config
dom.event.clipboardevents.enabled -> false

# 4. resize images in a directory
DIR="resized"
mkdir $DIR
for f in *.JPG; do
  mogrify -path $DIR -resize 50% $f
done

# 
