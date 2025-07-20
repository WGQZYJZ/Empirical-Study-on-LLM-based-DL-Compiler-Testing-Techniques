input_tensor = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.bool)
other = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.bool)
torch.Tensor.logical_xor_(input_tensor, other)