data = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9], [1, 3, 5, 9], [4, 3, 2, 9]], dtype=torch.long)
embedding_bag = torch.nn.EmbeddingBag(10, 2, mode='mean')
output = embedding_bag(data)