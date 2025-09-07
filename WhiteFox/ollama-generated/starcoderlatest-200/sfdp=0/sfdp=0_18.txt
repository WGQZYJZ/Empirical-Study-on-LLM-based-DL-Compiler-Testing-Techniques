
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.projection = torch.nn.Linear(512, 32) # Projection layer
        self.attention = torch.nn.MultiheadAttention(embed_dim=32, num_heads=4, dropout=0.0)
 
    def forward(self, q, k, v):
        projected_query = self.projection(q)
        projected_key   = self.projection(k)
        attention_weights = self.attention(projected_query, projected_key, projected_key)[0]
        output = attention_weights.matmul(v)
        return output


# Initializing the model
m = TransformerModel()

 # Inputs to the model
q  = torch.randn(16, 512, 4096) # Query tensor for the self-attention layer
k  = torch.randn(16, 512, 4096) # Key tensor for the self-attention layer
v  = torch.randn(16, 512, 4096) # Value tensor for the self-attention layer
