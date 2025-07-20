input_tensor = torch.randint(low=1, high=10, size=(3, 3), dtype=torch.int32)
other = torch.randint(low=1, high=10, size=(3, 3), dtype=torch.int32)
torch.Tensor.lcm_(input_tensor, other)