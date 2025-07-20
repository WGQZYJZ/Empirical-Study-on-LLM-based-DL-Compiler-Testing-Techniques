input_tensor = torch.randn(3, 2)
vec1 = torch.randn(2)
vec2 = torch.randn(3)
result = torch.Tensor.addr(input_tensor, vec1, vec2, beta=0.5, alpha=0.5)