
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, q, k, v):
        attention = self.attention(q, k, v)
        return attention

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
