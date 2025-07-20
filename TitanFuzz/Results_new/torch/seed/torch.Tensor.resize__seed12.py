input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.resize_(input_tensor, 6, 4)