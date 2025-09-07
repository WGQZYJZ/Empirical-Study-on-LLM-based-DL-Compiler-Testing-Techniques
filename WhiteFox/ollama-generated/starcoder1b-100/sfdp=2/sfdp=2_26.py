
class Model(torch.nn.Module):
    def __init__(self, dim=512, heads=8, layer_norm_epsilon=1e-6, drop_p=0.1):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, dim)
        self.layer_norm = torch.nn.LayerNorm(dim, eps=layer_norm_epsilon)
        self.attn = MultiHeadAttention(heads, dim, dropout_p=drop_p)
        self.proj = torch.nn.Linear(dim, dim)
        self.dropout = torch.nn.Dropout(drop_p)
 
    def forward(self, x1):
        v = self.embedding(x1).permute(2, 0, 1) # Convert (batch, seq_len, embedding_dim) to (seq_len, batch, embedding_dim)
        v = self.layer_norm(v)
        qk = torch.matmul(v, v.transpose(-2, -1))  # Compute the dot product of the query and the key
        k = qk / math.sqrt(float(dim)) # Scale the dot product by the square root of the embedding dimension
        attn_weights = self.attn(qk, k, v) # Perform attention on the scaled dot product (qk / sqrt(emb_dim))
        out = torch.matmul(attn_weights, v)  # Compute the dot product of the output of the softmax and the value (out = qk * attn_weights)
        out = self.dropout(self.proj(out))  # Apply dropout to the output
        return out


# Initializing the model
m = Model()


