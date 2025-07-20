input_tensor = torch.arange(1, 5)
vec2 = torch.arange(1, 3)
output_tensor = torch.Tensor.outer(input_tensor, vec2)