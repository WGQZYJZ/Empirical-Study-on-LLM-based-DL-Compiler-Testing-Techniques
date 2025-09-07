
class TransformerModel(torch.nn.Module):
    def __init__(self, nhead=10, dmodel=256, dff=384, dim=768, dropout=.1, maxlen = 499):
        super().__init__()
        self.dmodel = dmodel
        self.pos_enc = PositionalEncoding(dmodel, dropout)
        self.layernorm1 = torch.nn.LayerNorm(normalized_shape=[-2], eps=1e-6)

        self.attn = torch.nn.MultiheadAttention(
            d_model  = dim, 
            num_heads = nhead, 
            dropout   = dropout
        )
        self.ff   = FeedForward(dmodel=dim, hidden=dff).cuda()
        
        self.layernorm2 = torch.nn.LayerNorm(normalized_shape=[-2], eps=1e-6)
 
    def forward(self, input):

        bs = input.size(0)
        seqlen  = min(maxlen, input.size(-1))
        d = self.dmodel
        posenc = torch.zeros([bs*seqlen, d]).cuda()
        for i in range(input.size(-2)):
            t = torch.ones([bs*(i+1), 1]).float().div_(torch.pow(t, -0.5 * j / self.dmodel))
            posenc[i] = t.reshape([-1])

        # Apply the positional encoding to input tensor
        output  = self.layernorm2(self.pos_enc(input + posenc.cuda()))

        output, _attnscores = self.attn(output, output) 
        return self.ff(output), _attnscores, output

# Inputs for the model
query = torch.randn(1, 499, 256).cuda()
key   = query
attn_mask = torch.zeros([383*768+3]).cuda().byte()
attn_mask[0]  = True


# Initializing the model with random weights and bias
m = TransformerModel(nhead=1)

__output__, attnscores, posenc2 = m(query) # The model produces a tuple of output and scores, attnscores and posenc


