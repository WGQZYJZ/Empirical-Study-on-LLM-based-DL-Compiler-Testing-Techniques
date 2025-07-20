mat = torch.randn(3, 3)
vec = torch.randn(3)
result = torch.Tensor.addmv_(mat, vec)