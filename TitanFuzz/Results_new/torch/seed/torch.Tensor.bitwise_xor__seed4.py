input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
other = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
torch.Tensor.bitwise_xor_(input_tensor, other)