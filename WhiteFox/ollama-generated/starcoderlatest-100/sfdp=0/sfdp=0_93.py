
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (inv_scale * key.shape[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(batch_size, heads, length, width)
key   = torch.randn(batch_size, heads, length, width)
value = torch.randn(batch_size, heads, length, width)
