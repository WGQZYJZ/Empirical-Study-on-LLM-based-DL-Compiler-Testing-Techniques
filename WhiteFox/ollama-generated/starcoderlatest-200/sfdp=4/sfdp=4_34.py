
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Linear(3, 8) 
        self.key_layer   = torch.nn.Linear(3, 16) 
        self.value_layer = torch.nn.Linear(3, 16)
        self.attn_mask   = torch.zeros([1, 8], dtype=torch.float)
 
    def forward(self, qk): # qk is the concatenation of query and key vectors 
        v  = self.query_layer(qk[:1]) @ self.key_layer.transpose(-2, -1) / math.sqrt(qk.size(-1))
        v += self.attn_mask
        w  = torch.softmax(v, dim=-1)
        return (self.value_layer @ w).view([-1, 3])


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8)
x2 = torch.randn(4, 16)
qk = torch.cat((x1, x2), dim=-1).contiguous().view([-1, 16])
