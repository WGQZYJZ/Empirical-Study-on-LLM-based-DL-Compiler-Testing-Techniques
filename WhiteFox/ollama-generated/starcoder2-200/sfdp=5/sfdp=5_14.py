class ScaledDotProductAttentionWithDropout(torch.nn.Module):
    def __init__(self, d_model: int, dropout_p: float = 0., trainable_dropout=True) -> None:
        super().__init__()
        self._dropout = torch.nn.Dropout(dropout_p)
        self._norm = torch.nn.LayerNorm(d_model)
        if trainable_dropout and not isinstance(dropout_p, float):
            self._drop_p = torch.nn.Parameter(torch.full([1], dropout_p))

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask=None) -> Tuple[torch.Tensor]:
        d_k  = query.size(-1)
        scale_factor = math.sqrt(d_k)
        scaled_dot  = (query @ key.transpose(-2, -1)) / scale_factor

        if isinstance(self._drop_p, float):
            attn_weight  = torch.softmax(scaled_dot + attn_mask, dim=-1).clamp_(min=0., max=1.) * self._norm(query)
        else:
            dropout  = self._dropout
            drop_p  = self._drop_p[:, None]
            attn_weight  = torch.softmax(scaled_dot + attn_mask, dim=-1).clamp_(min=0., max=1.) * self._norm(query)
            scaled_dot += dropout(drop_p, tensor=attn_weight)
        output = attn_weight @ value

        return output
