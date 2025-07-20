input = torch.randn(10, 3)
index = torch.randint(low=0, high=3, size=(10,))
output = torch.index_select(input, dim=1, index=index)