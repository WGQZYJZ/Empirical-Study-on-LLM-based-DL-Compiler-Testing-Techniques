_input_tensor = torch.randint(low=0, high=10, size=(10,))
hist_without_range = torch.Tensor.histogram(_input_tensor, bins=10)
hist_with_range = torch.Tensor.histogram(_input_tensor, bins=10, range=(0, 10))