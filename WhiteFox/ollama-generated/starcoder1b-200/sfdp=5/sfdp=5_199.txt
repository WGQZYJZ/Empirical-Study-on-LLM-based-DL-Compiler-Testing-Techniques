
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size, embed_dim, num_layers=2):
        super().__init__()
 
        self.emb = torch.nn.Embedding(input_size, embed_dim)  # Use embedding to transform the query/key/value into vectors
        
        self.layer_norm1 = LayerNorm(embed_dim)
        self.dropout1 = nn.Dropout(p=0.2)
        self.attn = MultiheadAttention(
            embed_dim,  # Query and key share same dimension
            num_heads=8,  # The number of attention heads
            dropout=0.0)  # No dropout
        
        self.layer_norm2 = LayerNorm(embed_dim)
        self.dropout2 = nn.Dropout(p=0.2)
        self.dense = torch.nn.Linear(embed_dim, output_size)
 
    def forward(self, x1, x2):
        # The query is the same for all heads
        k = self.emb(x2).contiguous().view(-1, x1.shape[1], self.emb.embedding_dim)  # Compute the key of attention mechanism
        q = self.emb(x1).contiguous().view(-1, x2.shape[0], self.emb.embedding_dim)  # Compute the query of attention mechanism
        
        k = self.layer_norm1(k)
        v = self.attn(q, k, value=self.emb(x2))  # Dot product with keys and values, we compute the attention weights
        v = self.dropout2(v)
        o = torch.tanh(self.dense(v))  # Apply a linear function to the output of attention mechanism
        return o


# Initializing the model
m = Model(3, 8, 64)


