input_list = [1, 2, 3]
embedding_layer = torch.nn.Embedding(num_embeddings=5, embedding_dim=4)
output_tensor = embedding_layer(torch.tensor(input_list))