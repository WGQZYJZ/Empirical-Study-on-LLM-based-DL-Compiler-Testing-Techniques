_input_tensor = torch.randint(low=0, high=100, size=(100,), dtype=torch.int)
hist = torch.Tensor.histogram(_input_tensor, bins=10)