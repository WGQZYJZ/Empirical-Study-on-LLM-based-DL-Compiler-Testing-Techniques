
class Attention(torch.nn.Module):
    def __init__(self, dim: int = None, dropout: float = 0., attn_mask: Optional[Tensor] = None):
        super().__init__()
 
        self._dim  = dim if dim is not None else self._get_dim()
        self._attn = torch.nn.Linear(2 * self._dim + (1 if attn_mask is None else 0),
                                     self._dim)
        self._drop = torch.nn.Dropout(dropout)
        self.attn_mask  = attn_mask
 
    def _get_dim(self): ...
    # Returns the size of the model's hidden layer
 
    def forward(self, query: Tensor, key: Optional[Tensor] = None, value: Optional[Tensor] = None
                ) -> Tuple[Tensor]:
        