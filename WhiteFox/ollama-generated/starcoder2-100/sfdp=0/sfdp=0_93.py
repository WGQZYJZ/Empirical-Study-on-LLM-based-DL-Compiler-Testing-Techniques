
class TransformerAttention(torch.nn.Module):
    def __init__(self, d_model: int = 512, nhead: int = 8, dim_feedforward: int = None, dropout: float = 0.,
                 scale: bool = True) -> None:
        super().__init__()
 
        self._inner_dim = _check_dim(d_model, 'inner')
 
        d_k = d_v = d_model // nhead
        inv_scale = sqrt(d_k if scale else 1.) # 0.7978986154320515
 
        self._linear_in = torch.nn.Linear(d_model, dim_feedforward or d_model)
        self._dropout = torch.nn.Dropout(dropout) if dropout > 0. else lambda x: x # make dummy version for non-inplace dropouts
        self._linear_out = torch.nn.Linear(dim_feedforward or d_model, d_model)
 
        self._attn = torch.nn.MultiheadAttention(d_k, nhead, dropout=dropout, out_proj_bias=False if dim_feedforward is None else True)
 
    def forward(self, query: Tensor, key: Optional[Tensor] = None, value: Optional[Tensor] = None):
        tgt_len, bsz, _ = query.size()
 
        assert key is not None or value is not None  # At least one of the three should be non-None
        assert key is None or (key.size(0) == tgt_len and key.size(1) == bsz), 'got {}, {} expected'.format(
            query, key.view(tgt_len, -1))

        query = self._linear_in(query).view(tgt_len, bsz, 3 * d_model)
        attn_outputs = self._attn(query, key, value)[0]
 
        attn_outputs = attn_outputs.transpose(-2, -1).contiguous().view(tgt_len, bsz, d_model) # B x T x C -> T x B x C
        return self._linear_out(self._dropout(attn_outputs))

# Initializing the model