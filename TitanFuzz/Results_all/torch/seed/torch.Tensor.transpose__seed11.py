input_tensor = torch.randn(2, 3, 5)
output_tensor = torch.Tensor.transpose_(input_tensor, 0, 2)