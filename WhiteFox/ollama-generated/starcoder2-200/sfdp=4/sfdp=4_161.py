
class Attention(torch.nn.Module):
    def __init__(self, dim: int) -> None:
        super().__init__()
 
        self._query = torch.nn.Linear(dim, 128) # Apply a linear layer to the query tensor
        self._key = torch.nn.Linear(dim, 364) # Apply a linear layer to the key tensor
 
    def forward(self, query: Tensor, value: Tensor, attn_mask: Optional[Tensor] = None):
        