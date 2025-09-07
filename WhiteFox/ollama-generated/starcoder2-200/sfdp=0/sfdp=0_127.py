
class ScaledDotProductAttention(nn.Module):
    def __init__(self, d_k: int = 16) -> None:
        super().__init__()
        self.scale = nn.Parameter(torch.tensor(d_k ** -0.5))
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1) * self.scale).softmax(dim=-1) 
        output  = scaled_dot_product @ value # output = attention weights.matmul(value)
        return output


class Model(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.sdp = ScaledDotProductAttention()
 
    def forward(self, query1, key2, val3)  -> Tensor:
       v4  = self.sdp(query1, key2, val3)
       return v4

# Initializing the model and inputs to it
model  = Model().to('cpu')
x_q, x_k , x_v = torch.randn(100, 8, 8), torch.randn(500, 7, 7), torch.randn(200,9,9)
 
__output___ = model(x_q, x_k, x_v)

