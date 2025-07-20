input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.transpose_(input_tensor, 0, 1)
output_tensor = torch.transpose(input_tensor, 0, 1)