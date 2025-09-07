
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self,
                 scale_factor=1e-6):
        super().__init__()
        self.scale = torch.tensor(scale_factor)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, dropout_p: float = 0.) -> torch.Tensor:
        v1 = torch.matmul(query, key.transpose(-2, -1)) * self.scale
        v3 = v1.softmax(dim=-1)
        v5 = torch.nn.functional.dropout(v3, p=dropout_p)
 
        return v5 @ value
