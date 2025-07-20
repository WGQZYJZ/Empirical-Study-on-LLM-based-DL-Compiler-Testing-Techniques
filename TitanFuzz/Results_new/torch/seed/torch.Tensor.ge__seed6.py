input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
result = torch.Tensor.ge_(input_tensor, other)