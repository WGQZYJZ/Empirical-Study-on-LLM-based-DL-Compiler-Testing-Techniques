_input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output = torch.Tensor.xlogy(_input_tensor, other)