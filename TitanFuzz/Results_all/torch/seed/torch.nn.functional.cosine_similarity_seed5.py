x1 = torch.randn(10, 3)
x2 = torch.randn(10, 3)
cosine_similarity = torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)