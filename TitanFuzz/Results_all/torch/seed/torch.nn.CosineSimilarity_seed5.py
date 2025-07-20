np.random.seed(0)
x = torch.from_numpy(np.random.rand(3, 4))
y = torch.from_numpy(np.random.rand(3, 4))
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)