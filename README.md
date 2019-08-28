### About
This is a frontend for the collection of tools used by the zebra.

<br>

### Contents
| File | Description |
|---|---|
| `code_samples` | Folder containing inactive code.|
| `one_d_view.py` | Widget containing the 1D Mode.|
| `prepare_view.py` | Widget containing the Prepare Mode.|
| `tools.py` | Tools used by Widgets.|
| `two_d_view.py` | Widget containing the 2D Mode.|
| `welcome_view.py` | Widget containing the Welcome Screen.|
| `zebra.py` | Main Window of the application. Run from here.

<br>

### How To

##### Installation:
```
pip3 install pyqt5
pip3 install matplotlib
python3 ./zebra.py
```

##### Note about PyQt:
Every UI element (e.g. *Button*) is a *Widget*. 
A *Widget* can also have a *Layout* (e.g. *Grid*) 
and contain other *Widgets*. 

For example:
A *Tab* widget may contain an empty container widget.
The empty container widget may have the grid layout,
and contain a button on position (0,0) of said grid.

