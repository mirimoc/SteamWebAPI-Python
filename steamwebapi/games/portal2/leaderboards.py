# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.leaderboards import IPortal2Leaderboards
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class IPortal2Leaderboards_620(IPortal2Leaderboards):
    """Methods relating to Portal 2 Leaderboards."""

    def __init__(self, *args, **kwargs):
        """Initialize IPortal2Leaderboards, which initiales SteamWebAPI."""
        super(IPortal2Leaderboards_620, self).__init__(*args, **kwargs)
