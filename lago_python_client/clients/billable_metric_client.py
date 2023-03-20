from typing import ClassVar, Type

from pydantic import BaseModel

from .base_client import BaseClient
from ..models.billable_metric import BillableMetricResponse


class BillableMetricClient(BaseClient):
    API_RESOURCE: ClassVar[str] = 'billable_metrics'
    RESPONSE_MODEL: ClassVar[Type[BaseModel]] = BillableMetricResponse
    ROOT_NAME: ClassVar[str] = 'billable_metric'
