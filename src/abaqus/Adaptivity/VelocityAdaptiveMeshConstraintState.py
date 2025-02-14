from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .AdaptiveMeshConstraintState import AdaptiveMeshConstraintState


@abaqus_class_doc
class VelocityAdaptiveMeshConstraintState(AdaptiveMeshConstraintState):
    """The VelocityAdaptiveMeshConstraintState object stores the propagating data for an Arbitrary Lagrangian
    Eularian (ALE) style velocity adaptive mesh constraint in a step. One instance of this object is created
    internally by the VelocityAdaptiveMeshConstraint object for each step. The instance is also deleted
    internally by the VelocityAdaptiveMeshConstraint object. The VelocityAdaptiveMeshConstraintState object has
    no constructor or methods. The VelocityAdaptiveMeshConstraintState object is derived from the
    AdaptiveMeshConstraintState object.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]

        The corresponding analysis keywords are:

        - ADAPTIVE MESH CONSTRAINT
    """

    #: A Float specifying the velocity component in the 1-direction.
    v1: float | None = None

    #: A Float specifying the velocity component in the 2-direction.
    v2: float | None = None

    #: A Float specifying the velocity component in the 3-direction.
    v3: float | None = None

    #: A Float specifying the rotational velocity component about the 1-direction.
    vr1: float | None = None

    #: A Float specifying the rotational velocity component about the 2-direction.
    vr2: float | None = None

    #: A Float specifying the rotational velocity component about the 3-direction.
    vr3: float | None = None

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v1State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v2State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v3State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr1State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr2State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr3State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState
    #: object. Possible values
    #: are: NOT_YET_ACTIVE, CREATED, PROPAGATED, MODIFIED, DEACTIVATED, NO_LONGER_ACTIVE, TYPE_NOT_APPLICABLE
    #: INSTANCE_NOT_APPLICABLE, PROPAGATED_FROM_BASE_STATE, MODIFIED_FROM_BASE_STATE, DEACTIVATED_FROM_BASE_STATE,
    #: BUILT_INTO_MODES
    status: SymbolicConstant

    #: A String specifying the name of the amplitude reference. The String is empty if the
    #: adaptive mesh constraint has no amplitude reference.
    amplitude: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        v1: float | None = None,
        v2: float | None = None,
        v3: float | None = None,
        vr1: float | None = None,
        vr2: float | None = None,
        vr3: float | None = None,
        v1State: Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED] | None = None,
        v2State: Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED] | None = None,
        v3State: Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED] | None = None,
        vr1State: Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED] | None = None,
        vr2State: Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED] | None = None,
        vr3State: Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED] | None = None,
        amplitudeState: Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED] | None = None,
        status: Literal[
            C.NOT_YET_ACTIVE,
            C.PROPAGATED_FROM_BASE_STATE,
            C.DEACTIVATED_FROM_BASE_STATE,
            C.DEACTIVATED,
            C.MODIFIED_FROM_BASE_STATE,
            C.PROPAGATED,
            C.NO_LONGER_ACTIVE,
            C.CREATED,
            C.INSTANCE_NOT_APPLICABLE,
            C.BUILT_INTO_MODES,
            C.TYPE_NOT_APPLICABLE,
            C.MODIFIED,
        ]
        | None = None,
        amplitude: str = "",
    ):
        """The VelocityAdaptiveMeshConstraintState object stores the propagating data for an Arbitrary
        Lagrangian Eularian (ALE) style velocity adaptive mesh constraint in a step. One instance of this object
        is created internally by the VelocityAdaptiveMeshConstraint object for each step. The instance is also
        deleted internally by the VelocityAdaptiveMeshConstraint object. The VelocityAdaptiveMeshConstraintState
        object has no constructor or methods. The VelocityAdaptiveMeshConstraintState object is derived from the
        AdaptiveMeshConstraintState object.

        .. note::
            This function can be accessed by::

                mdb.models[name].steps[name].VelocityAdaptiveMeshConstraintState

        Parameters
        ----------
        v1
            A Float specifying the velocity component in the 1-direction.
        v2
            A Float specifying the velocity component in the 2-direction.
        v3
            A Float specifying the velocity component in the 3-direction.
        vr1
            A Float specifying the rotational velocity component about the 1-direction.
        vr2
            A Float specifying the rotational velocity component about the 2-direction.
        vr3
            A Float specifying the rotational velocity component about the 3-direction.
        v1State
            A SymbolicConstant specifying the propagation state of the velocity component in the  1-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        v2State
            A SymbolicConstant specifying the propagation state of the velocity component in the  2-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        v3State
            A SymbolicConstant specifying the propagation state of the velocity component in the  3-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        vr1State
            A SymbolicConstant specifying the propagation state of the rotational velocity component  about the
            1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        vr2State
            A SymbolicConstant specifying the propagation state of the rotational velocity component  about the
            2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        vr3State
            A SymbolicConstant specifying the propagation state of the rotational velocity component  about the
            3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        amplitudeState
            A SymbolicConstant specifying the propagation state of the amplitude reference. Possible  values are UNSET,
            SET, UNCHANGED, FREED, and MODIFIED.
        status
            A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState  object. Possible
            values  are:
            - NOT_YET_ACTIVE
            - CREATED
            - PROPAGATED
            - MODIFIED
            - DEACTIVATED
            - NO_LONGER_ACTIVE
            - TYPE_NOT_APPLICABLE
            - INSTANCE_NOT_APPLICABLE
            - PROPAGATED_FROM_BASE_STATE
            - MODIFIED_FROM_BASE_STATE
            - DEACTIVATED_FROM_BASE_STATE
            - BUILT_INTO_MODES
        amplitude
            A String specifying the name of the amplitude reference. The String is empty if the  adaptive mesh
            constraint has no amplitude reference.
        """
        super().__init__(amplitudeState, status, amplitude)
