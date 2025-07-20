input_tensor = torch.randn(2, 3)
vec1 = torch.randn(3)
vec2 = torch.randn(2)
output_tensor = torch.Tensor.addr(input_tensor, vec1, vec2, beta=1, alpha=1)