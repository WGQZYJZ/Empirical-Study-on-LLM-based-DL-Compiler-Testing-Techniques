x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([1, 1, 1, 1])
res = torch.ne(x, y)
res = torch.ne(x, y, out=torch.empty(4))