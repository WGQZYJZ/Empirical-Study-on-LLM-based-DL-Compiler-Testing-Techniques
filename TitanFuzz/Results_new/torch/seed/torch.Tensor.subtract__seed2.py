input_tensor = torch.rand(3, 2)
other_tensor = torch.rand(3, 2)
result_tensor = torch.Tensor.subtract_(input_tensor, other_tensor)