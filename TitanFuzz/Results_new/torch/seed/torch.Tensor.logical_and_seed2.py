input_tensor = torch.randint(0, 2, (2, 3, 4), dtype=torch.bool)
other = torch.randint(0, 2, (2, 3, 4), dtype=torch.bool)
torch.Tensor.logical_and(input_tensor, other)