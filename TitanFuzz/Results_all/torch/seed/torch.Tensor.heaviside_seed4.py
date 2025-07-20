input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.heaviside(input_tensor, 0)