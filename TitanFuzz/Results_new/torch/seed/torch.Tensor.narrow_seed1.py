input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.narrow(input_tensor, 1, 0, 2)