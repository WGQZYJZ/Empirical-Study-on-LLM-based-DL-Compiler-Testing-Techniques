x1 = torch.randn(1, 3)
x2 = torch.randn(1, 3)
y = torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)