
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
 
    def forward(self, query, key, value):
        attention_weights = self.attention(query, key, value)[0]
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / 30 ** 0.5
        output = scaled_dot_product.softmax(dim=-1).matmul(value)
        return attention_weights.matmul(output)


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 128, 320, 64)
key = torch.randn(2, 128, 320, 64)
value = torch.randn(2, 128, 320, 64)
