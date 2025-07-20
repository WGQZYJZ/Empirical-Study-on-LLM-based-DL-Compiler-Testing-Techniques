input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int)
other = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int)
torch.Tensor.bitwise_and_(input_tensor, other)