input = torch.randn(3, 4)
index = torch.tensor([0, 2])
result = torch.index_select(input, 0, index)