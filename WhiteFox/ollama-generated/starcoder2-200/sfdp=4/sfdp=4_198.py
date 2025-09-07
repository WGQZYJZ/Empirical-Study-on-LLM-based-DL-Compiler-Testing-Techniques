
class DotProductSelfAttention(torch.nn.Module):
    def __init__(self, hidden_size: int) -> None:
        super().__init__()
 
        self.linear = torch.nn.Linear(hidden_size, 128, bias=False)
 
    def forward(self, q: torch.Tensor, k: torch.Tensor) -> torch.Tensor:
        v  = torch.tanh(self.linear(k))
 
        qk  = q @ v.transpose(-2, -1) / math.sqrt(qk.size(-1)) + 1e-6
 

        attn_weight = torch.softmax(qk, dim=-1)
 
        return (attn_weight @ v).transpose(0, 1)

