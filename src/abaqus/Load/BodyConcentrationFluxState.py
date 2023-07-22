from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .LoadState import LoadState


@abaqus_class_doc
class BodyConcentrationFluxState(LoadState):
    """The BodyConcentrationFluxState object stores the propagating data for a BodyConcentrationFlux object in a
    step. One instance of this object is created internally by the BodyConcentrationFlux object for each step.
    The instance is also deleted internally by the BodyConcentrationFlux object. The BodyConcentrationFluxState
    object has no constructor or methods. The BodyConcentrationFluxState object is derived from the LoadState
    object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - CFLUX
    """

    #: A Float specifying the body concentration flux magnitude.
    magnitude: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the body concentration flux
    #: magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    magnitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    #: values are:
    #:
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: Optional[SymbolicConstant] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""