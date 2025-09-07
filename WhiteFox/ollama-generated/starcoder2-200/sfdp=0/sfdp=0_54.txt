
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale = 1e-4):
        super().__init__()
        self.inv_scale = inv_scale
    
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product = torch.matmul(query, key.transpose(-2,-1)) /  (torch.sqrt(torch.float32(key.shape[-1]) * self.inv_scale))

        attention_weights  =  scaled_dot_product.softmax(dim=-1)
        output = attention_weights .matmul(value)
        return output


# Initializing the model