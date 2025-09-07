
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(value.shape[-1])
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = torch.matmul(attention_weights, value)
        return output
 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.norm = torch.nn.LayerNorm([64])
 
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        v1 = self.conv(x1)
        v2 = self.norm(v1)
        