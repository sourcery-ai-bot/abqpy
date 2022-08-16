import typing

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry
from ...UtilityAndView.abaqusConstants import *


class ConstrainedSketchGeometryArray(typing.List[ConstrainedSketchGeometry]):
    """The ConstrainedSketchGeometryArray is a sequence of ConstrainedSketchGeometry objects.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import sketch
            mdb.models[name].sketches[name].geometry[i]
    """

    def findAt(self, coordinates: tuple, printWarning: Boolean = True) -> typing.Union[ConstrainedSketchGeometry, typing.List[ConstrainedSketchGeometry]]:
        """This method returns the ConstrainedSketchGeometry object located at the given
        coordinates.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**- and **Y**-coordinates of the object to find.
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object.
        """
        return ConstrainedSketchGeometry()
