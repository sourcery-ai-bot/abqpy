from __future__ import annotations

from typing import List, Sequence, Union, overload

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex import (
    ConstrainedSketchVertex,
)
from ..UtilityAndView.abaqusConstants import Boolean
from .Vertex import Vertex


@abaqus_class_doc
class VertexArray(List[Vertex]):
    """The VertexArray is a sequence of ConstrainedSketchVertex objects. If the part is modified, then
    VertexArray must be updated for that part.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].vertices
            mdb.models[name].parts[name].allSets[name].vertices
            mdb.models[name].parts[name].sets[name].vertices
            mdb.models[name].parts[name].vertices
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].sets[name].vertices
            mdb.models[name].rootAssembly.allInstances[name].vertices
            mdb.models[name].rootAssembly.allInternalSets[name].vertices
            mdb.models[name].rootAssembly.allSets[name].vertices
            mdb.models[name].rootAssembly.instances[name].sets[name].vertices
            mdb.models[name].rootAssembly.instances[name].vertices
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].vertices
            mdb.models[name].rootAssembly.modelInstances[i].vertices
            mdb.models[name].rootAssembly.sets[name].vertices
            mdb.models[name].rootAssembly.vertices
    """

    @abaqus_method_doc
    def __init__(self, vertices: list[Vertex]):
        """This method creates a VertexArray object.

        .. note::
            This function can be accessed by::

                part.VertexArray

        Parameters
        ----------
        vertices
            A list of ConstrainedSketchVertex objects.

        Returns
        -------
        VertexArray
            A VertexArray object.
        """
        ...

    @overload
    @abaqus_method_doc
    def findAt(
        self,
        coordinates: tuple[float, float, float],
        printWarning: Boolean = True,
    ) -> ConstrainedSketchVertex:
        ...

    @overload
    @abaqus_method_doc
    def findAt(
        self,
        coordinates: tuple[tuple[float, float, float],],
        printWarning: Boolean = True,
    ) -> list[ConstrainedSketchVertex]:
        ...

    @overload
    @abaqus_method_doc
    def findAt(
        self,
        *coordinates: tuple[tuple[float, float, float],],
        printWarning: Boolean = True,
    ) -> list[ConstrainedSketchVertex]:
        ...

    @abaqus_method_doc
    def findAt(self, *args, **kwargs) -> Union[ConstrainedSketchVertex, list[ConstrainedSketchVertex]]:
        """This method returns the object or objects in the VertexArray located at the given coordinates. findAt
        initially uses the ACIS tolerance of 1E-6. As a result, findAt returns any ConstrainedSketchVertex
        object that is at the arbitrary point specified or at a distance of less than 1E-6 from the arbitrary
        point. If nothing is found, findAt uses the tolerance for imprecise geometry (applicable only for
        imprecise geometric entities). findAt will always try to find objects among all the vertices in the part
        or assembly instance and will not restrict itself to a subset even if the VertexArray represents such
        subset.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**, **Y**, and **Z** coordinates of the object to
            find.findAt returns either a ConstrainedSketchVertex object or a sequence of ConstrainedSketchVertex objects based on the
            type of input.

            * If **coordinates** is a sequence of Floats, findAt returns the ConstrainedSketchVertex object at that point.

            * If you omit the **coordinates** keyword argument, findAt accepts as arguments a sequence of sequence
              of floats in the following format::

                verts = v.findAt(((20.19686, -169.513997, 27.798593), ),
                                ((19.657627, -167.295749, 27.056402), ),
                                ((18.274129, -157.144741, 25.15218), ))
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        ConstrainedSketchVertex
            A ConstrainedSketchVertex object or a sequence of ConstrainedSketchVertex objects..
        """
        first_arg = kwargs.get("coordinates", args[0] if args else ((),))
        return ConstrainedSketchVertex() if isinstance(first_arg[0], float) else [ConstrainedSketchVertex()]

    @overload
    @abaqus_method_doc
    def getSequenceFromMask(self, mask: str) -> ConstrainedSketchVertex:  # type: ignore
        ...

    @overload
    @abaqus_method_doc
    def getSequenceFromMask(self, mask: Sequence[str]) -> list[ConstrainedSketchVertex]:  # type: ignore
        ...

    @abaqus_method_doc
    def getSequenceFromMask(
        self, mask: Union[str, Sequence[str]]
    ) -> Union[ConstrainedSketchVertex, list[ConstrainedSketchVertex]]:  # type: ignore
        """This method returns the object or objects in the VertexArray identified using the specified **mask**.
        This command is generated when the JournalOptions are set to COMPRESSEDINDEX. When a large number of
        objects are involved, this method is highly efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        ConstrainedSketchVertex | list[ConstrainedSketchVertex]
            A ConstrainedSketchVertex object or a sequence of ConstrainedSketchVertex objects..
        """
        return ConstrainedSketchVertex() if isinstance(mask, str) else [ConstrainedSketchVertex()]

    @abaqus_method_doc
    def getMask(self) -> str:
        """This method returns a string specifying the object or objects.

        Returns
        -------
        str
            A String specifying the object or objects.
        """
        return ""

    @abaqus_method_doc
    def getByBoundingBox(
        self,
        xMin: float = 0,
        yMin: float = 0,
        zMin: float = 0,
        xMax: float = 0,
        yMax: float = 0,
        zMax: float = 0,
    ) -> VertexArray:
        """This method returns an array of vertex objects that lie within the specified bounding box.

        Parameters
        ----------
        xMin
            A float specifying the minimum **X** boundary of the bounding box.
        yMin
            A float specifying the minimum **Y** boundary of the bounding box.
        zMin
            A float specifying the minimum **Z** boundary of the bounding box.
        xMax
            A float specifying the maximum **X** boundary of the bounding box.
        yMax
            A float specifying the maximum **Y** boundary of the bounding box.
        zMax
            A float specifying the maximum **Z** boundary of the bounding box.

        Returns
        -------
        VertexArray
            A VertexArray object, which is a sequence of ConstrainedSketchVertex objects..
        """
        return VertexArray([Vertex()])

    @abaqus_method_doc
    def getByBoundingCylinder(self, center1: tuple, center2: tuple, radius: str) -> VertexArray:
        """This method returns an array of vertex objects that lie within the specified bounding cylinder.

        Parameters
        ----------
        center1
            A tuple of the **X**, **Y**, and **Z** coordinates of the center of the first end of the
            cylinder.
        center2
            A tuple of the **X**, **Y**, and **Z** coordinates of the center of the second end of the
            cylinder.
        radius
            A float specifying the radius of the cylinder.

        Returns
        -------
        VertexArray
            A VertexArray object, which is a sequence of ConstrainedSketchVertex objects..
        """
        return VertexArray([Vertex()])

    @abaqus_method_doc
    def getByBoundingSphere(self, center: tuple, radius: str) -> VertexArray:
        """This method returns an array of vertex objects that lie within the specified bounding sphere.

        Parameters
        ----------
        center
            A tuple of the **X**, **Y**, and **Z** coordinates of the center of the sphere.
        radius
            A float specifying the radius of the sphere.

        Returns
        -------
        VertexArray
            A VertexArray object, which is a sequence of ConstrainedSketchVertex objects..
        """
        return VertexArray([Vertex()])

    @abaqus_method_doc
    def getBoundingBox(self) -> dict[str, tuple[float, float, float]]:
        """This method returns a dictionary of two tuples representing minimum and maximum boundary values of
        the bounding box of the minimum size containing the vertex sequence.

        Returns
        -------
        dict[str, tuple[float, float, float]]
            A Dictionary object with the following items:

            - **low**: a tuple of three floats representing the minimum **X** -, **Y** -, and **Z** -boundary
              values of the bounding box.
            - **high**: a tuple of three floats representing the maximum **X** -, **Y** -, and **Z** -boundary
              values of the bounding box.
        """
        return {"low": (0.0, 0.0, 0.0), "high": (0.0, 0.0, 0.0)}

    @abaqus_method_doc
    def getClosest(self, coordinates: tuple, searchTolerance: str = "") -> dict[int, tuple[Vertex, tuple]]:
        """This method returns a object or objects in the VertexArray closest to the given set of points, where
        the given points need not lie on ConstrainedSketchVertex objects in the VertexArray.

        Parameters
        ----------
        coordinates
            A sequence of a sequence of floats, where each sequence of floats describes the **X**,
            **Y**, and **Z** coordinates of a point::

                >>> r=v.getClosest(coordinates=((20.0, 20.0, 10.0),(-1.0, -15.0, 15), ))
                >>> r.keys()
                [0, 1]
                >>> r[0]
                (mdb.models['Model-1'].parts['Part-1'].vertices[0], (15.7090625762939, 29.1666641235352, 20.0))
        searchTolerance
            A double specifying the distance within which the closest object must lie. The default
            value is half of the parent part/instance size.

        Returns
        -------
        dict
            This method returns a dictionary object. The key to the dictionary object is the
            position of the input point in the tuple specified in the **coordinates** starting at
            index 0. If a closest vertex could be found then the value is a sequence consisting of
            two objects. The first object in the sequence is a ConstrainedSketchVertex that is close to the input
            point referred to by the key. The second object in the sequence is a sequence of floats
            that specifies the **X**, **Y**, and **Z**  location of the ConstrainedSketchVertex. See program listing
            above.

        Raises
        ------
        Error
            The mask results in an empty sequence, An exception occurs if the resulting sequence is empty.
        """
        return {0: (Vertex(), (0.0, 0.0, 0.0))}
