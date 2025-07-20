input_tensor = torch.randint(low=0, high=10, size=(5, 3), dtype=torch.float)
result = torch.Tensor.greater_equal_(input_tensor, 5)