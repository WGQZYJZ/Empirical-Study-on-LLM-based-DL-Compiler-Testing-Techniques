
class Attention(torch.nn.Module):
    def __init__(self, d_model, num_heads, dropout=0., attn_mask=None):
        super().__init__()

        self.d_model = d_model
        self.num_heads = num_heads
        self.attn_drop = torch.nn.Dropout(dropout)
        self.query = torch.nn.Linear(d_model, d_model)
        self.key = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)

        if attn_mask is not None:
            attn_mask = attn_mask.to(torch.bool).masked_fill_(attn_mask != 0., False)

            def _create_padding(x):
                return -2 ** 32 + torch.tensor(1, device=x.device)
            pad = [_create_padding(x) for x in (attn_mask)]

        self._set_attn_mask(attn_mask)

    def forward(self, query, key, value, attn_mask=None):
        q = self.query(query).view(*query.size()[:-1], self.num_heads, -1)  # (N, S, H, D)
        k = self.key(key).view(*key.size()[:-1], self.num_heads, -1) / math.sqrt(self.d_model)

        if attn_mask is not None:
            k += pad[0]  # B x num_head x slen x slen
            q += pad[1]  # B x num_head x rlen x d_model

        k = k.permute(2, 3, 0, 1).contiguous().view(-1, self.d_model)
        v = self.value(value).view(*value.size()[:-1], -1) / math.sqrt(self.d_model)
        
        v_slen = value.size(-2)  # slen = rlen of value
        k_rlen = key.size(-2)

        if attn_mask is not None:
            mask = self._attn_mask[0] - pad[0] + torch.arange(v_slen, device=q.device).unsqueeze(-1).expand(k_rlen, v_slen) # (slen, rlen) -> [slen, slen]

            attn = torch.matmul(
                torch.tanh(torch.einsum('bihkd,dh->bhid', q, k)),  # [H, slen x rlen]
                torch.softmax(mask[None], -1),
            )
        else:
            attn = torch.einsum('ihkd,hd->hiad', q, k)
        
        output = self.attn_drop(torch.einsum('bihsa,bhsd->bhia', attn, v).contiguous().view(*value.size()[:-2], -1))
        return output, attn

