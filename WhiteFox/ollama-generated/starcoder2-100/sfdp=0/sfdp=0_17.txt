
class TransformerBlock(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.attention = torch.nn.MultiheadAttention(embed_dim, num_heads)

    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(embed_dim) # Scaled dot product attention
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        
        return output


# Initializing the model
model = TransformerBlock()

# Inputs to the model
query = torch.randn(batch_size, 30, embed_dim).to('cuda')
key = query
value = key

