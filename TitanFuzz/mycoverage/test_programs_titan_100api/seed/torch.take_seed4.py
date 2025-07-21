input = torch.randn(4, 6)
index = torch.LongTensor([[0, 1], [2, 3]])
output = torch.take(input, index)