from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Leaf import Leaf
from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant


@abaqus_class_doc
class LeafFromModelElemLabels(Leaf):
    """The LeafFromModelElemLabels object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromModelElemLabels object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    #: A sequence of Strings specifying expressions that denote element labels per part
    #: instance in the model. Each part instance element expression is a sequence of a String
    #: specifying the part instance name and a sequence of element expressions; for example,
    #: `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element
    #: expressions can be any of the following:An Int specifying a single element label; for
    #: example, `1`.A String specifying a single element label; for example, `'7'`.A String
    #: specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`.
    elementLabels: tuple

    @abaqus_method_doc
    def __init__(self, elementLabels: tuple):
        """This method creates a Leaf object from a sequence of element labels spanning several
        part instances.

        .. note:: 
            This function can be accessed by::

                LeafFromModelElemLabels

        Parameters
        ----------
        elementLabels
            A sequence of Strings specifying expressions that denote element labels per part
            instance in the model. Each part instance element expression is a sequence of a String
            specifying the part instance name and a sequence of element expressions; for example,
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The element
            expressions can be any of the following:An Int specifying a single element label; for
            example, `1`.A String specifying a single element label; for example, `'7'`.A String
            specifying a sequence of element labels; for example, `'3:5'` and `'3:15:3'`.

        Returns
        -------
        LeafFromModelElemLabels
            A :py:class:`~abaqus.DisplayGroup.LeafFromModelElemLabels.LeafFromModelElemLabels` object.
        """
        super().__init__(DEFAULT_MODEL)
