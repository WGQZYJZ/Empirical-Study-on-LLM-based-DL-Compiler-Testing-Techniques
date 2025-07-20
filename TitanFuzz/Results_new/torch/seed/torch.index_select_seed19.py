input = torch.randn(3, 5)
index = torch.tensor([1, 2, 0, 2, 1])
output = torch.index_select(input, 1, index)