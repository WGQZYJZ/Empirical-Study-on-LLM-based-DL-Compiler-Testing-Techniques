
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=8, num_heads=4)
 
    def forward(self, query, key, value, scale=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (scale ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 8, 64, 64)
key = torch.randn(3, 8, 128, 128)
value = torch.randn(3, 8, 128, 128)
