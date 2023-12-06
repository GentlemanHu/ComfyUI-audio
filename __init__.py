import folder_paths

from .util_nodes import (
    NODE_CLASS_MAPPINGS as UTIL_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as UTIL_NODE_DISPLAY_NAME_MAPPINGS,
)
from .musicgen import (
    NODE_CLASS_MAPPINGS as MGAC_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as MGAC_NODE_DISPLAY_NAME_MAPPINGS,
)
from .musicgen_hf import (
    NODE_CLASS_MAPPINGS as MGHF_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as MGHF_NODE_DISPLAY_NAME_MAPPINGS,
)
from .tortoise import (
    NODE_CLASS_MAPPINGS as TORTOISE_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as TORTOISE_NODE_DISPLAY_NAME_MAPPINGS,
)


NODE_CLASS_MAPPINGS = {
    **UTIL_NODE_CLASS_MAPPINGS,
    **MGAC_NODE_CLASS_MAPPINGS,
    **MGHF_NODE_CLASS_MAPPINGS,
    **TORTOISE_NODE_CLASS_MAPPINGS,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    **UTIL_NODE_DISPLAY_NAME_MAPPINGS,
    **MGAC_NODE_DISPLAY_NAME_MAPPINGS,
    **MGHF_NODE_DISPLAY_NAME_MAPPINGS,
    **TORTOISE_NODE_DISPLAY_NAME_MAPPINGS,
}
