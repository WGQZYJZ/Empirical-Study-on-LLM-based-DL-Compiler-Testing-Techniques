
class Attention(torch.nn.Module):
    def __init__(self, inv_sqrt_dim=None):
        super().__init__()
        self.inv_scale = torch.tensor(1.).float() if inv_sqrt_dim is None else torch.tensor([inv_sqrt_dim]).float().sqrt()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor) -> tuple[torch.Tensor]:
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(key)
 
        return output

model  = Attention()

