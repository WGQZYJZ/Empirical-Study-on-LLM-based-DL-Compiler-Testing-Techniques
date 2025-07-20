input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.int32)
other = torch.randint(0, 2, (3, 3), dtype=torch.int32)
torch.Tensor.bitwise_xor_(input_tensor, other)