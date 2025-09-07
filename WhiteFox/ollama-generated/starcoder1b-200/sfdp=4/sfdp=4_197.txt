
class Model(torch.nn.Module):
    def __init__(self, embed_dim=128, num_heads=4, dim_feedforward=2048, dropout=0.1):
        super().__init__()
        self.query = torch.nn.Linear(embed_dim, embed_dim)
        self.key = torch.nn.Linear(embed_dim, embed_dim)
        self.value = torch.nn.Linear(embed_dim, embed_dim)
        self.layer_norm1 = LayerNorm(embed_dim)
        self.layer_norm2 = LayerNorm(embed_dim)
        self.dropout = nn.Dropout(p=dropout)
 
    def forward(self, query, key):
        # Compute the dot product of the query and key
        attn  = torch.matmul(query, key).squeeze(-1)
        # Normalize the attention weights before applying softmax
        attn  = self.softmax(attn)
        # Get the output of the attention layer
        out = torch.matmul(attn, self.value)
        # Scale the output back to the original input size using a linear projection and dropout
        out  = self.layer_norm1(out + self.dropout((self.query.weight * attn).contiguous().view(-1, out.size(-1))))
        return out
 

# Initializing the model
m = Model()


