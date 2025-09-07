
class Model(torch.nn.Module):
    def __init__(self, embedd_dim, num_heads, ff_dim):
        super().__init__()
        self.qk = torch.nn.Linear(embedd_dim, embedd_dim)  # Apply the linear transformation to the input embedding dimensions
        self.attn = nn.MultiheadAttention(embedd_dim, num_heads, dropout=0.1)  # Configure multi-head attention with dropout rate of 0.1 and the embedding dimensionality
        self.ffn = torch.nn.Linear(embedd_dim, ff_dim)  # Apply the linear transformation to the input embedding dimensions

    def forward(self, query):
        v1 = self.qk(query)  # Compute the dot product of the query and key (plus an attention mask), followed by a dropout operation
        v2 = torch.softmax(v1, dim=-1)
        v3 = attn_weight @ value # Apply dropout to the softmax output
        v4 = v2 @ v3 # Compute the dot product of these attention weights and the value
        return v4


# Initializing the model
m  = Model(embedd_dim, num_heads, ff_dim)
 
 
