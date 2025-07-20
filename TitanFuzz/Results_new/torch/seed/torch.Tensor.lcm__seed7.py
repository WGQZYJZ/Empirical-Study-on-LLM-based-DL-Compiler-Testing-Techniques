input_tensor = torch.randint(low=0, high=10, size=(5, 5), dtype=torch.int32)
other_tensor = torch.randint(low=0, high=10, size=(5, 5), dtype=torch.int32)
torch.Tensor.lcm_(input_tensor, other_tensor)