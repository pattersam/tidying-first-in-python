import importlib
import pkgutil


ALL_TIDYINGS = sorted(
    [
        importlib.import_module(".".join([__name__, tidying.name]))
        for tidying in pkgutil.iter_modules(__path__)
    ],
    key=lambda k: str(k.__doc__),
)
