### About
This is a frontend for the collection of tools used by the zebra.

<br>

### Contents
| File | Description |
|---|---|
|`wiondow.py`  | The main window. Run from here.|

<br>

### How To

##### Installation:
```
pip3 install pyqt5
pip3 install matplotlib
python3 ./window.py
```

##### About PyQt
Every UI element (e.g. *Button*) is a *Widget*. 
A *Widget* can also have a *Layout* (e.g. *Grid*) 
and contain other *Widgets*. 

For example:
A *Tab* widget may contain an empty container widget.
The empty container widget may have the grid layout,
and contain a button on position (0,0) of said grid.

