
class Model(torch.nn.Module):
    def __init__(self, query_size, key_size, embedding_dim):
        super().__init__()
 
        self.query = torch.nn.Linear(query_size, embedding_dim)
        self.key = torch.nn.Linear(key_size, embedding_dim)
        self.value = torch.nn.Linear(embedding_dim, embedding_dim)
 
    def forward(self, query, key):
        qk = self._attention(query, key)
        v  = self._attention(key, value)
        return qk @ v

    def _attention(self, query, key):
        d1 = torch.matmul(query, self.query.weight)  # Apply linear transformation to the query
        d2 = torch.matmul(key, self.key.weight)    # Apply linear transformation to the key
        scores = (d1 * d2).sum(-1) / math.sqrt(query.size(-1))   # Compute the dot product of the query and key
        return scores


# Initializing the model with 64 for query_size, 128 for key_size, and 32 for embedding_dim.
m = Model(query_size=64, key_size=128, embedding_dim=32)

# Inputs to the model
q = torch.randn(8, 32, 64, 64)   # Input query
k = torch.randn(8, 32, 128, 64)  # Input key
v = torch.randn(8, 32, 128, 64)  # Input value


# Output of the model
out = m(q, k)


