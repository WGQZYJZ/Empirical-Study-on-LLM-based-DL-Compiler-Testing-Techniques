input = torch.randn(4, 6, dtype=torch.float)
index = torch.tensor([1, 2, 0, 3])
src = torch.zeros(4, 3)
output = torch.scatter(src, 0, index.unsqueeze(1).expand(4, 3), input)