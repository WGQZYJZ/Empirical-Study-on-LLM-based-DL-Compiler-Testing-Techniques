data = [[1, 2, 4, 5], [4, 3, 2, 9]]
embedding = torch.nn.EmbeddingBag(10, 3, mode='mean')
input = torch.tensor(data)
output = embedding(input)