
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self._inv_scale = 1 / torch.sqrt(d_k)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) * self._inv_scale
 
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
 
        return output


# Initializing the model
sdpa = ScaledDotProductAttention()


# Inputs to the model
key = torch.randn(4, 6000, d_k=250)
query = torch.randn(3, 80, d_k=1250)
value = torch.randn(4, 720, 512)


# Output of the model:
output  = sdpa(query, key, value)

