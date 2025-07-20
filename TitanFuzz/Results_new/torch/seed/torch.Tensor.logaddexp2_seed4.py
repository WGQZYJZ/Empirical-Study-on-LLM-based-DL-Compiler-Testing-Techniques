input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output_tensor = torch.Tensor.logaddexp2(input_tensor, other)