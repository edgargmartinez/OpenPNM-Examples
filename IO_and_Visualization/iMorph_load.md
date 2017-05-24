# iMorph Import Example

(http://imorph.fr/)[iMorph] is a image analysis software that is available as a free download.  It happens to include a network extraction tool that is especially well suited to foams and other high porosity media.  The following example shows how to import a network from the files that are created by iMorph.

## Open Spyder and import OpenPNM

``` python
>>> import scipy as sp
>>> import OpenPNM as op


```

## Import Files
The following assumes that the two files provided by iMorph have not been renamed ("throats_cellsThroatsGraph_Nodes.txt" and "throats_cellsThroatsGraph.txt"), and are stored together in a folder called ``iMorph-Sandstone`` in a directory called ``fixtures``.  

``` python
>>> import os
>>> path = os.path.join('fixtures', 'iMorph-Sandstone')
>>> pn = op.Utilities.IO.iMorph.load(path=path)
>>> pn.name = 'berea'

```

> **Note**: The exact will change depending on the relative locations of your files so you'll have to learn how to construct the path for your system.

## Inspect Network

Once the network is imported as an OpenPNM network, you can begin playing with it.  In the image below, is a nice shiny Paraview rendering of the network.  Export to Paraview and visualizing is explained in [this example](https://github.com/PMEAL/OpenPNM-Examples/blob/master/IO_and_Visualization/view_vtp_in_paraview.md)

![](https://i.imgur.com/Bqq71Lk.png)

There seems to be some strange topology in this particular network, with many isolated pores and two different scales of pore sizes. The pore sizes are not a problem for OpenPNM, but the disconnected clusters of pores cause trouble for the solvers (i.e. singular matrices).  This *health* of a network can be checked as follows:

``` python
>>> h = pn.check_network_health()
>>> len(h['isolated_pores'])
28

```
In this case there are 28 pores that are completely isolated (i.e. no exactly 0 neighbors).  These can be trimmed from the network as follows:

``` python
>>> op.Network.tools.trim(network=pn, pores=h['isolated_pores'])
>>> h = pn.check_network_health()
>>> len(h['isolated_pores'])
0

```

The network still has other problems, but isolated pores is not one of them.  
