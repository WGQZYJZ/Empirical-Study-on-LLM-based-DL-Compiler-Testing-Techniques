x = torch.rand(2, 3, dtype=torch.float32)
y = torch.rand(2, 3, dtype=torch.float64)
result = torch.promote_types(x.dtype, y.dtype)