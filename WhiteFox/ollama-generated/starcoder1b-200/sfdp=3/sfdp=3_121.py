
class Model(torch.nn.Module):
    def __init__(self, embed_dim=100):
        super().__init__()
        self.embed = torch.nn.EmbeddingBag(num_embeddings=num_embeddings, embedding_dim=embed_dim)
 
    def forward(self, x1):
        v  = self.embed(x1)
        return v


# Initializing the model
m = Model()

# Inputs to the model
# Embedding bag representation of [input] and weight matrix [weight] will be computed.
x1 = torch.randn(1, 3, embed_dim=embed_dim)
w1 = torch.randn(1, embed_dim, embed_dim)
