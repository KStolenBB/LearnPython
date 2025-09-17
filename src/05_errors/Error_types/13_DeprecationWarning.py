"""DeprecationWarning
Demonstration of a DeprecationWarning using the warnings module.

DeprecationWarning indicates that a feature is deprecated and will likely be
removed in a future version. It is not an error and execution continues unless
warnings of this category are configured to be shown or turned into errors.
"""

import warnings

warnings.warn(
    "This feature is deprecated and will be removed in a future version.",
    DeprecationWarning,
)

print("DeprecationWarning issued.")
