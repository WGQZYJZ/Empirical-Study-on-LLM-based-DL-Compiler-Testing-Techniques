x = torch.randn(5, 5)
y = torch.tensor([1, 2, 3, 4, 5])
z = torch.promote_types(x.dtype, y.dtype)