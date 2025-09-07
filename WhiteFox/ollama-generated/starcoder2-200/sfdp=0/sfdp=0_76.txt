
class Attention(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, dim_k=None, dropout=0.1, bias=True,
                 add_bias_kv=False, add_zero_attn=False, kdim=None, vdim=None, scale=False):
        super().__init__()
        self._qkv_same_embed = False
        self._compute_scale = scale
 
        self.dropout = torch.nn.Dropout(p=dropout)
        assert d_model % nhead == 0, 'd_model must be divisible by nhead'
 
    def forward(self, query: Tensor, key: Optional[Tensor] = None, value: Optional[Tensor] = None,
                attn_mask: Optional[Tensor] = None, key_padding_mask: Optional[Tensor] = None) -> Tuple[Tensor]:
        ...

# Initializing the model
m  = Attention(d_model=512, nhead=8)

 # Inputs to the model
query = torch.randn(30, 64, 7*7)
key   = torch.randn(30, 64, 7*7)
value = torch.randn(30, 64, 7*7)
__output__, __weight_matrix__  = m(query, key=key, value=value)

 