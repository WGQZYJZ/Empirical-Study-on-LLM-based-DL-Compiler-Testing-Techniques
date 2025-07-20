input = torch.randn(3, 4)
output = torch.index_select(input, 1, torch.LongTensor([0, 2]))