input_tensor = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
result = torch.Tensor.logaddexp2(input_tensor, other)