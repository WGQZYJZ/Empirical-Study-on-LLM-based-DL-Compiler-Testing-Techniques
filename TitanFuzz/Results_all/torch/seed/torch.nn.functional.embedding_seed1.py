input_data = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
embedding_weight = torch.randn(10, 3)
embedding = torch.nn.functional.embedding(input_data, embedding_weight)