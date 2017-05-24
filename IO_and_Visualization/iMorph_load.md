    def test_load_imorph(self):
        path = os.path.join(FIXTURE_DIR, 'iMorph-Sandstone')
        net = io.iMorph.load(path)
        assert net.Np == 1518
        assert net.Nt == 2424
        assert sp.shape(net['pore.coords']) == (1518, 3)
        assert sp.shape(net['throat.conns']) == (2424, 2)
        a = {'pore.volume', 'pore.types', 'throat.volume', 'throat.types'}
        assert a.issubset(net.props())
        a = {'pore.internal', 'pore.top_boundary', 'pore.bottom_boundary',
             'pore.front_boundary', 'pore.back_boundary', 'pore.left_boundary',
             'pore.right_boundary'}
        assert a.issubset(net.labels())


# iMorph Import Example

(http://imorph.fr/)[iMorph] is a image analysis software that is available as a free download.  It happens to include a network extraction tool that is especially well suited to foams and other high porosity media.  The following example shows how to import a network from the files that are created by iMorph.

## Open Spyder and import OpenPNM

``` python
>>> import scipy as sp
>>> import OpenPNM as op


```

## Import Files
The following assumes that two files provided by iMorph have not been renamed ("throats_cellsThroatsGraph_Nodes.txt" and "throats_cellsThroatsGraph.txt"), and are stored in a folder called ``iMorph-Sandstone`` in a directory called ``fixtures``

``` python
>>> import os
>>> path = os.path.join('fixtures', 'iMorph-Sandstone')
>>> pn = op.Utilities.IO.iMorph.load(path=path)
>>> pn.name = 'berea'

```
