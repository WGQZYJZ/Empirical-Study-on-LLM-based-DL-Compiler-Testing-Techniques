x1 = torch.rand(2, 3)
x2 = torch.rand(2, 3)
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
y = cosine_similarity(x1, x2)