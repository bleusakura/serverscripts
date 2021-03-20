for id in `deluge-console "info" | grep "^ID: " | sed -En "s/ID: //p"`; do deluge-console "rm $id"; done
