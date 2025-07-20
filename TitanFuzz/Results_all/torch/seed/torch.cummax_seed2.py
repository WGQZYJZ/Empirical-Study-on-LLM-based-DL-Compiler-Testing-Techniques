input = torch.randint(low=0, high=10, size=(3, 5), dtype=torch.int32)
output = torch.cummax(input, dim=1)