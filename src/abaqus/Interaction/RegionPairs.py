from abaqusConstants import *


class RegionPairs:
    """The RegionPairs object stores the domain pair definition for ContactExp and ContactStd
    objects. The RegionPairs object has no constructor or members.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].interactions[name].excludedPairs
            mdb.models[name].interactions[name].includedPairs

        The corresponding analysis keywords are:

        - CONTACT INCLUSIONS
                - CONTACT EXCLUSIONS
    """

    def setValuesInStep(
        self,
        stepName: str,
        useAllstar: Boolean = OFF,
        addPairs: SymbolicConstant = None,
        removePairs: SymbolicConstant = None,
    ):
        """This method allows addition and removal of domain pairs in a given step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the region pair assignments are to be
            modified.
        useAllstar
            A Boolean specifying whether the contacting surface pair consists of all exterior faces
            and -- in an Abaqus/Explicit analysis -- analytical rigid surfaces, shell edges, and
            beam segments in the model.
        addPairs
            A sequence of pairs of region objects or SymbolicConstants that specify the surface
            pairs to add to the included pairs of the ContactExp or ContactStd object in the given
            step. Possible values of the SymbolicConstants are GLOBAL and SELF. When used with a
            ContactExp object, the second parameter of each pair can also be a string that
            references an Eulerian material surface.
        removePairs
            A sequence of pairs of region objects or SymbolicConstants that specify the surface
            pairs to remove from the included pairs of the ContactExp or ContactStd object in the
            given step. Possible values of the SymbolicConstants are GLOBAL and SELF. When used with
            a ContactExp object, the second parameter of each pair can also be a string that
            references an Eulerian material surface.
        """
        ...
