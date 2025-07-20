input = torch.arange(0, 12).reshape(3, 4)
index = torch.LongTensor([0, 2])
output = torch.index_select(input, 0, index)