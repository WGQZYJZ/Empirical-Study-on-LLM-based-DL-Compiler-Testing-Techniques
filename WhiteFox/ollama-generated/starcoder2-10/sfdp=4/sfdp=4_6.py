
class SelfAttentionLayer(nn.Module):
    def __init__(self, dim, heads=8, dim_head=-1, dropout=0., causal=False, kdim=-1):
        super().__init__()
        self.attn = MultiHeadAttention(heads, dim, dropout)
 
    def forward(self, query: Tensor, key: Optional[Tensor], value: Optional[Tensor] = None) -> Tensor:
        return self.attn((query, key), (value))


# Initializing the model