
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim: int = 32):
        super().__init__()
        self.dim = dim
        self.scale = torch.rsqrt(torch.tensor([self.dim]))
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) * self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


m_scaled = ScaledDotProductAttention()

# Inputs to the model
query  = torch.randn([4,32])
key    = query / 2 + torch.randn([32,4096])/1e-7 # Invariant to scaling, divide by 2 before normalizing to avoid numerical error
value  = key * 2

