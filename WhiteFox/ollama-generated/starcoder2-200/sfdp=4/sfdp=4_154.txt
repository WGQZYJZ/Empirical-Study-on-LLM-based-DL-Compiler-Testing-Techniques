
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._sqrt = torch.sqrt
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        q_k = (query @ key.transpose(-2, -1)) / self._sqrt(key.size(-1))
 
        return softmax(q_k + attn_mask) @ value


# Initializing the model 
m = ScaledDotProductAttention()
 
# Inputs to the model
query = torch.randn(64, 50, 250)
key   = query
value = torch.randn(64, 128, 513)

 # Model execution
