i = torch.tensor([[0, 1, 1], [2, 0, 2]])
v = torch.tensor([3, 4, 5], dtype=torch.float32)
s = torch.sparse.FloatTensor(i, v, torch.Size([3, 3]))
r = torch.sparse.sum(s, dim=1)