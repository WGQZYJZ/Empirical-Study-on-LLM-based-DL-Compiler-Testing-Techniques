input_tensor = torch.randn(4, 4)
vec1 = torch.randn(4)
vec2 = torch.randn(4)
output_tensor = torch.Tensor.addr(input_tensor, vec1, vec2)