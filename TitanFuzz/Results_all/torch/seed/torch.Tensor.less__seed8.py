input_tensor = torch.randn(3, 5)
other = torch.randn(3, 5)
output_tensor = torch.Tensor.less_(input_tensor, other)