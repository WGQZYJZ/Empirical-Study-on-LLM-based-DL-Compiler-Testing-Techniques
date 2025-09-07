
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale: float = 10000.) -> None:
        super().__init__()
        self._inv_scale = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)  # (batch x query len x value len)
        return output

# Initializing the model
sdpa = ScaledDotProductAttention()

 # Inputs to the model
query = torch.randn(4, 5, 320)
key = torch.randn(4, 5, 60)
value = torch.randn(4, 5, 198)
__output__  = sdpa(query, key, value)

