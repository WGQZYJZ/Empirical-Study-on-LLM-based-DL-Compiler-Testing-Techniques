input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
result = torch.Tensor.subtract(input_tensor, other_tensor)
result = torch.Tensor.subtract(input_tensor, other_tensor, alpha=0.5)