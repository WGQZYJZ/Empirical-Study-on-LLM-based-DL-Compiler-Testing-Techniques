input_tensor = torch.randint(0, 10, (10,))
result = torch.Tensor.bincount(input_tensor, minlength=10)