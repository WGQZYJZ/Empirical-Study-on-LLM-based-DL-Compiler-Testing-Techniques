input_data = torch.randn(3, 4)
vec1 = torch.randn(4)
vec2 = torch.randn(3)
output = torch.Tensor.addr(input_data, vec1, vec2)