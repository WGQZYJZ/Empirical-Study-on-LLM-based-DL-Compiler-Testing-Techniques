
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(2,4)
        self.key   = torch.randn(3,5)
        self.value = torch.randn(10,784)
 
    def forward(self):
        attn_mask  = self.query > -float('inf')
        qk        = self.query @ self.key.transpose(-2,-1)/ math.sqrt(self.query.size(-1))
        attn_weight= torch.softmax(qk + attn_mask, dim=-1)
        return  attn_weight@self.value


# Initializing the model
m = Model()


# Inputs to the model
__input__ = m()


