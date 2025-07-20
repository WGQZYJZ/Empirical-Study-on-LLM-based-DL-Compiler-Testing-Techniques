a = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.uint8)
b = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.uint8)
c = torch.bitwise_xor(a, b)