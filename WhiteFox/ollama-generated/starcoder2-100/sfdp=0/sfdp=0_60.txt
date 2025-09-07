
class TransformerAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(embedding_dim, embedding_dim)
        self.query = torch.nn.Linear(embedding_dim, embedding_dim)
 
    def forward(self, query, key, value):
 
        # Scaling factor
        inv_scale  = math.sqrt(query.size(-1))
 
        # Compute scaled dot product
        scaled_dot_product  = torch.matmul(
            self.key(key), self.query(query).transpose(-2, -1) / inv_scale
        )
 
        # Apply softmax to get attention weights
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
 
        return output

# Initializing the model
m  = TransformerAttention()


# Inputs to the model
query   = torch.randn(4, 32)
key    = torch.randn(64000 * embedding_dim).view(-1, 64000, embedding_dim)
value   = torch.randn(64000 * embedding_dim).view(-1, 64000, embedding_dim)

