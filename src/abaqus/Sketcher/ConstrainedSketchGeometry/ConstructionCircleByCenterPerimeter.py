import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class ConstructionCircleByCenterPerimeter(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, center: typing.Tuple[float, ...], point1: typing.Tuple[float, ...]):
        """This method constructs a construction circle using a center point and a point on the
        perimeter. The circle is added to the geometry repository of the ConstrainedSketch
        object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].ConstructionCircleByCenterPerimeter

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the construction circle.
        point1
            A pair of Floats specifying a point on the perimeter of the construction circle.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the circle cannot be created).

        """
        ...
