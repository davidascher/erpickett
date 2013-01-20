for f in *.jpg; do gm convert -size 256x256 $f -resize 256x256 ../thumb/$f; done

