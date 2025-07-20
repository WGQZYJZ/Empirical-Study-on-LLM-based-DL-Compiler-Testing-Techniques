data = torch.randn(3, 3)
vec1 = torch.randn(3)
vec2 = torch.randn(3)
output = torch.Tensor.addr(data, vec1, vec2)