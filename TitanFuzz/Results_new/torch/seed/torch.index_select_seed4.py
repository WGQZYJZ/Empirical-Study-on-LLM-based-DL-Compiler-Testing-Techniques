input = torch.randn(3, 4)
index = torch.tensor([0, 2])
output = torch.index_select(input, dim=0, index=index)
output = torch.index_select(input, dim=1, index=index)