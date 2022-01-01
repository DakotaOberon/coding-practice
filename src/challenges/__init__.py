from src.Challenge import ChallengeGroup
from src.challenges.ChainDecorators import ChainDecorators
from src.challenges.CheckClassOrSubclass import CheckClassOrSubclass
from src.challenges.CheckEmptyList import CheckEmptyList
from src.challenges.CheckIfInstanceOf import CheckIfInstanceOf
from src.challenges.FlatList import FlatList
from src.challenges.GetLastInList import GetLastInList
from src.challenges.OutputParameters import OutputParameters
from src.challenges.SwitchValues import SwitchValues
from src.challenges.SetGlobalInFunction import SetGlobalInFunction
from src.challenges.GetMethodsOfClass import GetMethodsOfClass


GROUP = ChallengeGroup()
GROUP.add(
    SwitchValues(),
    GetLastInList(),
    FlatList(),
    CheckEmptyList(),
    CheckClassOrSubclass(),
    ChainDecorators(),
    CheckIfInstanceOf(),
    OutputParameters(),
    SetGlobalInFunction(),
    GetMethodsOfClass()
)
