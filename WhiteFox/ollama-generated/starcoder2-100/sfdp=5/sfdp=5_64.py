
class Model(torch.nn.Module):
    def __init__(self, dropout =0.25):
        super().__init__()
 
        self.query  = torch.nn.Parameter(torch.randn(16))
        self.key   = torch.nn.Parameter(torch.randn(3, 8))
        self.value = torch.nn.Parameter(torch.randn(4096, 256*8))
 
        self.attn_mask = torch.nn.Parameter(torch.rand((1, 3, 3)))
 
    def forward(self):
        qk  = self.query @ self.key.transpose(-2, -1) / math.sqrt(query.size(-1)) 
        qk +=  self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
 
        output = attn_weight @ value
        return v6
