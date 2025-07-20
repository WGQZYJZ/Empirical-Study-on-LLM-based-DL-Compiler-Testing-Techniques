x = torch.randn(4, 3, 5, 5, 5)
lazy_batch_norm = torch.nn.LazyBatchNorm3d(3)
y = lazy_batch_norm(x)