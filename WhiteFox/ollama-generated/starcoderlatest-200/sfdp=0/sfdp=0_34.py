
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=128)
 
    def forward(self, x1, key, value, scale=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (scale or 10000)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Inputs to the model
x1, key, value, scale = torch.randn(2, 4, 64), torch.randn(2, 4, 64, 64), torch.randn(2, 4, 64, 64), 5000
