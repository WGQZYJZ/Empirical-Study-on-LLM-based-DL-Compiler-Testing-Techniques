
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key2, value3):
         v0 = torch.matmul(query1, key2.transpose(-2,-1))
         v1  = v0.div(inv_scale_factor)
         v4 =  torch.nn.functional.dropout(v1, p=p) 
         return v4
# Initializing the model
m  = Model()
 
# Inputs to the model
q1  = torch.randn(256, 8*8*2048)
k2 = torch.randn(256, 768)
v3  = torch.randn(256, 768)
 
# The initial output value of the model should be different from the previous one
__output__  = m(q1, k2, v3)

