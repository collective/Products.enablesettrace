from . import monkeypatch  # noqa

import AccessControl


AccessControl.ModuleSecurityInfo("pdb").declarePublic("set_trace")
