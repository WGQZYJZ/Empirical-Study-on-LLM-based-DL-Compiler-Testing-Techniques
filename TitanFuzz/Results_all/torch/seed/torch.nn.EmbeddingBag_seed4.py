data = [[1, 2, 4, 5], [4, 3, 2, 9]]
data = torch.tensor(data)
embedding_bag = torch.nn.EmbeddingBag(10, 3, mode='mean')
embedding_bag(data)