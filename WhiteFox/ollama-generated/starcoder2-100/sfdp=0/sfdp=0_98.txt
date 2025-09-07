
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale: float = 1) -> None:
        super().__init__()
        self.inv_scale  = inv_scale
 
    @staticmethod
    def scaled_dot_product(query, key, value):
         scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
         return scaled_dot_product
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product  = ScaledDotProductAttention.scaled_dot_product(query, key, value)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model with invscale=50
m  = ScaledDotProductAttention() # 50

# Inputs to the model
q1  = torch.randn(2, 384)
k1  = torch.randn(2, 384)
v1  = torch.randn(2, 384)

 __output__  = m(q1, k1, v1)


