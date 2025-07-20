input_tensor = torch.randn(3, 5)
vec1 = torch.randn(5)
vec2 = torch.randn(3)
result = torch.Tensor.addr(input_tensor, vec1, vec2, beta=1, alpha=1)