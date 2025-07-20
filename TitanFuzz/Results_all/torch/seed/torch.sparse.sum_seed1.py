input = Variable(torch.sparse.FloatTensor(torch.LongTensor([[0, 1], [1, 0]]), torch.randn(2), torch.Size([2, 2])))
torch.sparse.sum(input, dim=None, dtype=None)