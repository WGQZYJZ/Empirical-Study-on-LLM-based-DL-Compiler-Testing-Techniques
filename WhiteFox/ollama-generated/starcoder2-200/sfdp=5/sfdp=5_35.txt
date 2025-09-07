
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        if not self._has_attentions:
            return self._default_forward(query)
 
        qk = torch.einsum('btd,td->btk', [query, key]) / math.sqrt(query.size(-1))
        if attn_mask is not None:
            qk += attn_mask
 
        qk  = torch.softmax(qk, dim=-1) # softmax
        qk   = F.dropout(qk, p=attn_p, training=self._training)
 
        return self._default_forward(qk @ value)
