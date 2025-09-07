
class AttentionLayer(nn.Module):
    def __init__(self, dim, num_heads=16, causal=False, dropout=0., bias=True):
        super().__init__()

        self.causal = causal

        self.to_qkv  = nn.Linear(dim, dim * 3, bias)
        self.attn = nn.Softmax(-1)

        if causal:
            raise NotImplementedError()
        
        self.to_out = nn.Linear(dim, dim, bias=bias)
        self._reset_parameters()
        self.norm01 = nn.LayerNorm(self.to_qkv(None).shape[-2:], eps=1e-6, elementwise_affine=False)


    def _reset_parameters(self):
      stdv  = 1 / math.sqrt(self.to_qkv.weight.shape[0])
        nn.init.uniform_(self.to_out.weight, -stdv, stdv)
        nn.init.zeros_(self.to_out.bias)

        self.attn = nn.MultiheadAttention(dim=self.to_qkv(None).shape[-1], 
                                      num_heads=4, # number of heads
                                      dropout=0.,  
                                      bias=True
                                     )

    def forward(self, x):
        