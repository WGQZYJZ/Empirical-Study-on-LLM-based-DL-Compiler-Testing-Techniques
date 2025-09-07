
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        attn  = torch.softmax((query @ query.transpose(-2,-1) / math.sqrt(query.size(-1))), dim=-1) 
        return attn @ torch.randn(32,8000), 9, None, None
 
 
# Initializing the model
m = Model()
 
# Inputs to the model (q and k)
q1 = torch.randn(32,64)
k1 = torch.randn(32,512,64) # key_embed

## Initial inputs to the model (query and key)
__inputs__ = [torch.randn(32, 64), None]

