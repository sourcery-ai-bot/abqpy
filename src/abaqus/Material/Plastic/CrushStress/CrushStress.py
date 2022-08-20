import typing

from .CrushStressVelocityFactor import CrushStressVelocityFactor
from ....UtilityAndView.abaqusConstants import *
from ...._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class CrushStress:
    """The CrushStress object specifies the crush stress of a material.


    .. note::
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].crushStress
            import odbMaterial
            session.odbs[name].materials[name].crushStress

        The table data for this object are:

        - Scaling factor.
        - Relative velocity.

        The corresponding analysis keywords are:

        - CRUSH STRESS
    """

    #: A sequence of sequences of Floats specifying the items described below.
    crushStressTable: typing.Tuple[typing.Tuple[float, ...]]

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    # An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    #: A :py:class:`~abaqus.Material.Plastic.CrushStress.CrushStressVelocityFactor.CrushStressVelocityFactor` object.
    crushStressVelocityFactor: CrushStressVelocityFactor = CrushStressVelocityFactor(
        ((),)
    )

    @abaqus_method_doc
    def __init__(
        self,
        crushStressTable: typing.Tuple[typing.Tuple[float, ...]],
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a CrushStress object.

        .. note::
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].CrushStress
                session.odbs[name].materials[name].CrushStress

        Parameters
        ----------
        crushStressTable
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        self.crushStressTable = crushStressTable
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies

    @abaqus_method_doc
    def setValues(
        self,
        crushStressTable: typing.Tuple[typing.Tuple[float, ...]] = ((),),
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a CrushStress object.

        .. note::
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].CrushStress
                session.odbs[name].materials[name].CrushStress

        Parameters
        ----------
        crushStressTable
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        """
        self.crushStressTable = crushStressTable
        self.temperatureDependency = temperatureDependency
        self.dependencies = dependencies
