low = 0
high = 100
size = (3, 3)
result = torch.randint(low, high, size)
result = torch.randint(low, high, size, dtype=torch.int64)