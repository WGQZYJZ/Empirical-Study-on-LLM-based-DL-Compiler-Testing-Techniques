input = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int32)
output = torch.all(input, dim=0)