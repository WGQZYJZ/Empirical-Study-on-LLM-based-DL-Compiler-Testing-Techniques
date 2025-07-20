input_data = Variable(torch.randn(3, 5))
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
cosine_similarity(input_data, input_data)