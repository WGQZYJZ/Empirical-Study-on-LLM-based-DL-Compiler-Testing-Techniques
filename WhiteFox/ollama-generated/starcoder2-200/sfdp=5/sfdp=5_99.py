
class Model(torch.nn.Module):
    def __init__(self, attn_weight=0.25):
        super().__init__()
 
        self.query = torch.nn.Parameter(torch.randn((384,), requires_grad=True))
        self.key = torch.nn.Parameter(torch.randn((768,), requires_grad=True))
        self.value  = torch.nn.Parameter(torch.randn((2048, 1), requires_grad=True))

        self.attn_mask  = torch.ones(768, 384)
        self._reset()
 
    def forward(self):
        v1  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) 
        v1  = qk + attn_mask
        v2  = torch.softmax(v1, dim=-1)
        v3  = torch.dropout(attn_weight, dropout_p, True) 
        v4  = v2 @ value
        return v4
    
    def _reset():
        self.query = nn.init.normal_(self.query, mean=0., std=.02)
        self.key  = nn.init.normal_(self.key, mean=0., std=.02)
        self.value  = nn.init.normal_(self.value, mean=0., std=.02)


# Initializing the model
m = Model(attn_weight=0.15)


# Inputs to the model
x1 = torch.randn((768)) # query
x2 = torch.randn((384)) # key 
x3 = torch.randn((384, 768)) # attn mask 

m(x1)