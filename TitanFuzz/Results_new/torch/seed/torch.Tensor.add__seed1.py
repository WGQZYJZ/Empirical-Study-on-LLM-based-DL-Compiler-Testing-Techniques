input_tensor = torch.randn(2, 3)
other = torch.randn(3)
output_tensor = torch.Tensor.add_(input_tensor, other)