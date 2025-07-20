input_tensor = torch.randint(10, (2, 3))
other = torch.randint(10, (2, 3))
result = torch.Tensor.not_equal(input_tensor, other)