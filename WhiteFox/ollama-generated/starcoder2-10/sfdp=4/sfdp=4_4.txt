
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(2, 3)
        self.key   = torch.randn(2, 4) 
        self.value = torch.randn(2, 3, 10, 10)
 
    def forward(self, mask):
 
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1) 
        output = attn_weight @ value
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
mask  = torch.ones(3,4,5).to(torch.int8)
x1  = m(mask)


