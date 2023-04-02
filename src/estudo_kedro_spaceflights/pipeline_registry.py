"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines() # Este comando faz com que os pipelines criados nas pastas pipelines sejam automaticamente adicionados ao pipeline registry
    pipelines["__default__"] = sum(pipelines.values()) # Este cria um pipeline __default__ que será rodado toda vez que o 'kedro run' for chamado sem mais nenhum argumento
    return pipelines
