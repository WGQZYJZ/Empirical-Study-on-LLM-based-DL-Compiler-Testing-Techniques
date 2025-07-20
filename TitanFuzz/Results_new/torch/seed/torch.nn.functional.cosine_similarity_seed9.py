x1 = torch.randn(4, 3)
x2 = torch.randn(4, 3)
result = torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)
result = torch.nn.functional.cosine_similarity(x1, x2, dim=0, eps=1e-08)