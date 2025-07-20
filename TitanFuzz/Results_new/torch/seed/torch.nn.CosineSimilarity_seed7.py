input_data = Variable(torch.randn(2, 3))
input_data = Variable(torch.randn(2, 3))
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cosine_similarity(input_data, input_data)