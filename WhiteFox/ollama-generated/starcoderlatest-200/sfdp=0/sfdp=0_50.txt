
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
attention = ScaledDotProductAttention()
q = torch.randn(56, 2048, dtype=torch.float32) # (batch size, nhead * heads, dim per head)
k = torch.randn(128, 2048, dtype=torch.float32) # (batch size, nhead * heads, dim per head)
v = torch.randn(56, 2048, dtype=torch.float32) # (batch size, nhead * heads, dim per head)
inv_scale = 1. / torch.sqrt(k.shape[-1])


# Inputs to the model
