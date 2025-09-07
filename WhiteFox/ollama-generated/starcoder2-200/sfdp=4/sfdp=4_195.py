
class DotProductAttention(torch.nn.Module):
    def __init__(self, causal=False):
        super().__init__()
        self.causal  = causal

    def forward(self, query, key, value, attn_mask=None):
 
        if not hasattr(self, "softmax"):
            dim  = -1 if self.causal else -2
            self.softmax  = torch.nn.Softmax(dim)
        dim0_size, dim1_size  =  query.size()[:2]
        key  = key / math.sqrt(query.size(-1))
        qk  = query @ key.transpose(-2, -1)

        if self.causal:
            ones   = torch.ones([dim0_size, 1, dim1_size],
                                dtype=torch.uint8, device=qk.device)

            lower  = torch.tril(ones, -1 + qk.ndimension())
            upper  = torch.triu(zeros, qk.ndimension() - 2)
        else:
            lower  = None
            upper  = None

        mask   = None if not attn_mask else lower * upper * (attn_mask == 0).to(dtype=torch.uint8)
        if mask is not None and mask.any():
            qk[mask]  = -1e9

        output  = self.softmax(qk)[..., :dim1_size, :dim1_size].transpose(-2, -1) @ value
        return output


# Initializing the model
m  = DotProductAttention()
 
# Inputs to the model
query  = torch.randn([40, 65536], dtype=torch.float32)
key    = torch.randn([40, 65536], dtype=torch.float32)
value  = torch.randn([40, 65537], dtype=torch.float32)


