input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.swapaxes(input_tensor, 0, 1)