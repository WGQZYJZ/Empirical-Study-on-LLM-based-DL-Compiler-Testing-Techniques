
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.Softmax(-1)
 
    def forward(self, xq, k, v):
       attn  = (xq @ k.transpose(-2,-1)) / math.sqrt(xq.size(-1)) 
       attn  = attn + attn_mask
       attn_weights  = self.attn(attn) 
       out  = torch.sum(attn_weights*v,dim=1)
        return out

# Initializing the model
m  = Model()

# Inputs to the model (query tensor, key tensor, and value tensor)
xq   = torch.randn(32,64,512); k = torch.randn(32,64,512) ; v=torch.randn(32,64,512)

