
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._scale  = torch.sqrt(torch.Tensor([d_k])).item()
 
    def forward(self, query: torch.tensor, key: torch.tensor, value: torch.tensor) -> torch.tensor:
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self._scale
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        output  = attention_weights.matmul(value)  
        return output


m  = ScaledDotProductAttention()

# Inputs to the model