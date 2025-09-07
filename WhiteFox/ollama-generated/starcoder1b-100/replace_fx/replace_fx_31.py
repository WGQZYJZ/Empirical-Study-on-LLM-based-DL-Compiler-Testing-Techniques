Note that the `Model` class can be extended by any other object which provides the required functionality and inherits from `Model`. This includes but is not limited to, `DataParallel`, `DistributedDataParallel`, `DDP` (with `sync_batches=True`) and a number of other objects.

