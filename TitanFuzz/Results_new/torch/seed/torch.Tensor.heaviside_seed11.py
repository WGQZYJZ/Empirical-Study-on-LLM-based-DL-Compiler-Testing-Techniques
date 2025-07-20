input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.heaviside(input_tensor, 0.5)