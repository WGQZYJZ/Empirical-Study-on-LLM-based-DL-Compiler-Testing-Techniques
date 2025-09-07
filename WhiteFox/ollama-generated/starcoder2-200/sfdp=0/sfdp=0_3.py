
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, embed_dim=512, inv_scale=None):
        super().__init__()
        self.inv_scale = 0 if inv_scale is None else float(inv_scale)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights @ value
        return output


# Initializing the model
m  = ScaledDotProductAttention()

# Inputs to the model
query   = torch.randn(64, 8, 50, 50)
key     = torch.randn(64, 128, 50, 50)
value   = torch.randn(64, 32, 50, 50)
 
