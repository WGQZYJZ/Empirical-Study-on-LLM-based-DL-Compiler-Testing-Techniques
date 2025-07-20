_input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.float32)
other = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.float32)
torch.Tensor.logical_and(_input_tensor, other)