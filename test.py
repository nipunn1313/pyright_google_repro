# firestore doesn't have py.typed - only firestore_v1 has
from google.cloud.firestore import AsyncClient  # type: ignore

from google.cloud.firestore_v1 import AsyncClient

from google.protobuf.descriptor import FieldDescriptor
