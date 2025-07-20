input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.transpose_(input_tensor, 0, 1)