input_tensor = torch.rand(2, 3)
vec1 = torch.rand(3)
vec2 = torch.rand(2)
output_tensor = torch.Tensor.addr(input_tensor, vec1, vec2)