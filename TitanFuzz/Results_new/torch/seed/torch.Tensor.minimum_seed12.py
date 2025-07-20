_input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
output = torch.Tensor.minimum(_input_tensor, other)