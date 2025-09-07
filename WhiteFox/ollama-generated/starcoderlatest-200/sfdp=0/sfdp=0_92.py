
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, query, key, value):
        dot_product = torch.matmul(query, key.transpose(-2, -1)) / (math.sqrt(self.dim))
        attention_weights = torch.softmax(dot_product, dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = ScaledDotProductAttention(64)

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 3, 64, 64)
value = torch.randn(1, 3, 64, 64)
