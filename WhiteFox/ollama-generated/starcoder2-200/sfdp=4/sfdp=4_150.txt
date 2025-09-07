
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key  = torch.randn(10, 32) 
        self.value= torch.randn(10, 4, 64, 64)
 
    def forward(self, query):
        v1 = self.query @ self.key / math.sqrt(self.key.size(-1)) 
        v2 = self.attn_mask + v1 
        v3 = torch.softmax(v2, dim=-1) 
        v4 = output 
return v6
