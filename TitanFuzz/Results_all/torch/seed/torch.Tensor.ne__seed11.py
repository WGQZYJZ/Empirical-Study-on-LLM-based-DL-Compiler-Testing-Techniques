_input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
result = torch.Tensor.ne_(_input_tensor, other)