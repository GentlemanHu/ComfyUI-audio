import folder_paths

from .util_nodes import (
    NODE_CLASS_MAPPINGS as UTIL_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as UTIL_NODE_DISPLAY_NAME_MAPPINGS,
)


try:
    from .musicgen_nodes import (
        NODE_CLASS_MAPPINGS as MGAC_NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as MGAC_NODE_DISPLAY_NAME_MAPPINGS,
    )
except Exception as e:
    print(f"WARNING: ComfyUI-audio failed to import musicgen nodes; reason: {e}")
    MGAC_NODE_CLASS_MAPPINGS = {}
    MGAC_NODE_DISPLAY_NAME_MAPPINGS = {}


try:
    from .musicgen_hf_nodes import (
        NODE_CLASS_MAPPINGS as MGHF_NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as MGHF_NODE_DISPLAY_NAME_MAPPINGS,
    )
except Exception as e:
    print(f"WARNING: ComfyUI-audio failed to import musicgen_hf nodes; reason: {e}")
    MGHF_NODE_CLASS_MAPPINGS = {}
    MGHF_NODE_DISPLAY_NAME_MAPPINGS = {}


try:
    from .tortoise_nodes import (
        NODE_CLASS_MAPPINGS as TORTOISE_NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as TORTOISE_NODE_DISPLAY_NAME_MAPPINGS,
    )
except Exception as e:
    print(f"WARNING: ComfyUI-audio failed to import tortoise nodes; reason: {e}")
    TORTOISE_NODE_CLASS_MAPPINGS = {}
    TORTOISE_NODE_DISPLAY_NAME_MAPPINGS = {}


try:
    from .valle_x_nodes import (
        NODE_CLASS_MAPPINGS as VEX_NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as VEX_NODE_DISPLAY_MAPPINGS,
    )
except Exception as e:
    print(f"WARNING: ComfyUI-audio failed to import vall_e_x; reason: {e}")
    VEX_NODE_CLASS_MAPPINGS = {}
    VEX_NODE_DISPLAY_MAPPINGS = {}


try:
    from .tacotron_nodes import (
        NODE_CLASS_MAPPINGS as TT2_NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as TT2_NODE_DISPLAY_NAME_MAPPINGS,
    )
except Exception as e:
    print(f"WARNING: ComfyUI-audio failed to import tacotron nodes; reason: {e}")
    TT2_NODE_CLASS_MAPPINGS = {}
    TT2_NODE_DISPLAY_NAME_MAPPINGS = {}


NODE_CLASS_MAPPINGS = {
    **UTIL_NODE_CLASS_MAPPINGS,
    **MGAC_NODE_CLASS_MAPPINGS,
    **MGHF_NODE_CLASS_MAPPINGS,
    **TORTOISE_NODE_CLASS_MAPPINGS,
    **VEX_NODE_CLASS_MAPPINGS,
    **TT2_NODE_CLASS_MAPPINGS,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    **UTIL_NODE_DISPLAY_NAME_MAPPINGS,
    **MGAC_NODE_DISPLAY_NAME_MAPPINGS,
    **MGHF_NODE_DISPLAY_NAME_MAPPINGS,
    **TORTOISE_NODE_DISPLAY_NAME_MAPPINGS,
    **VEX_NODE_DISPLAY_MAPPINGS,
    **TT2_NODE_DISPLAY_NAME_MAPPINGS,
}
