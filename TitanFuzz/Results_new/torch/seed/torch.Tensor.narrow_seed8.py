input_tensor = torch.randn(1, 10)
output_tensor = torch.Tensor.narrow(input_tensor, 1, 0, 5)