input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.uint8)
other = torch.randint(0, 2, (2, 3), dtype=torch.uint8)
torch.Tensor.bitwise_and_(input_tensor, other)