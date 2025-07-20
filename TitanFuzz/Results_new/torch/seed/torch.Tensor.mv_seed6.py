input_tensor = torch.randn(3, 4)
vec = torch.randn(4)
output_tensor = torch.Tensor.mv(input_tensor, vec)