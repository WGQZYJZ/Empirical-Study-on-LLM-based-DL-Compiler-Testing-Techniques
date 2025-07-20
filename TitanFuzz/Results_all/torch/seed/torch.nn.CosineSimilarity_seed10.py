input_data = [Variable(torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), Variable(torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))]
cosine_similarity = torch.nn.CosineSimilarity(dim=0, eps=1e-08)