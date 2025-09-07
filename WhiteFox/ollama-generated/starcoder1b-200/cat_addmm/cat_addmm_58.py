
class Model(torch.nn.Module):
    def __init__(self, embedding_dim, num_layers, dropout_p):
        super().__init__()
        self.embedding = torch.nn.EmbeddingBag(num_embeddings=2651, embed_dim=embedding_dim, sparse=True)
 
    def forward(self, x1, x2, dim):
        v1  = torch.addmm(x1, x2, dim)  # Perform a matrix multiplication of x1 and x2 and add it to the input
        v2 = self.embedding(v1).view(-1, self.embedding.num_embeddings)  # Convert the embeddings into batches of vectors
        v3 = torch.cat([x2], dim)  # Concatenate the result along a specified dimension
        return torch.addmm(x2, x2, v2).view(x2.size(0), -1)  # Sum up the two representations and then convert to single-dimensional vectors


# Initializing the model
m = Model()


