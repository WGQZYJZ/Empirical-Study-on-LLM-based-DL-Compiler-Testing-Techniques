
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=1.0):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = ScaledDotProductAttention()

# Inputs to the model
query  = torch.randn(2, 8, 64, 32)
key    = torch.randn(12, 8, 64, 32)
value  = torch.randn(12, 8, 64, 32)
