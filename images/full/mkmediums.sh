for f in *.jpg; do gm convert -size 800x800 $f -resize 800x800 ../medium/$f; done

