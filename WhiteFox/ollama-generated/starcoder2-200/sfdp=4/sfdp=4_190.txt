
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mask = None
 
    def forward(self, query, key, value):
        # Compute the scaled dot product of the query and key tensors.
        attn = torch.einsum('...at,...a->...ta', [query, key]) / math.sqrt(query.size(-1))

        if self.mask is not None:
            attn = attn + self.mask

        # Compute softmax over the time dimension of the attention weights and
        # compute a weighted sum of the value tensor using these weights.
        attn_weights  = torch.softmax(attn, dim=-2)
        return attn_weights @ value

m1  = ScaledDotProductAttention()

