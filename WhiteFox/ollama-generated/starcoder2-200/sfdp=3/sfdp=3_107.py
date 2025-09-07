
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, qk, v, scale=0.5, dropout=0.1):
        v1  = self.attn(qk, v)[0]
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(48, 256) 
key   = torch.randn(38, 256) + query
v     = torch.randn(38, 10, 768)
 
# Initializing a new scale factor and dropout parameter to the model
scale = 0.9 # Any number other than 1 will work fine as long as the model can handle this
dropout_p = 0.52
 
__output__  = m(query, key, v, scale=scale, dropout=dropout_p)
