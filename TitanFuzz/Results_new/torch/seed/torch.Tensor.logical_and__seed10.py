_input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.bool)
other = torch.randint(0, 2, (3, 3), dtype=torch.bool)
torch.Tensor.logical_and_(_input_tensor, other)