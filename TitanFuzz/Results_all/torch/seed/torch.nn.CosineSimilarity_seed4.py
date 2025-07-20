x = torch.randn(4, 3)
y = torch.randn(4, 3)
cos = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos(x, y)