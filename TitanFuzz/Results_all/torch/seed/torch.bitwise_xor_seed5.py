input = torch.randint(low=0, high=2, size=(1, 4), dtype=torch.int32)
output = torch.bitwise_xor(input, input)