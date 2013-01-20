for f in *.jpg; do gm convert -gravity center -size 256x256 $f -resize 256x256^  -extent 256x256 ../thumb/$f; done

