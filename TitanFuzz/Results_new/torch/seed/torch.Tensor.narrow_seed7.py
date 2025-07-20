input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.narrow(input_tensor, 1, 1, 2)