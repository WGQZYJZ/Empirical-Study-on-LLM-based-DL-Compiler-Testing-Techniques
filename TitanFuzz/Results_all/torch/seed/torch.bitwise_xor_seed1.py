input = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
other = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
out = torch.bitwise_xor(input, other)