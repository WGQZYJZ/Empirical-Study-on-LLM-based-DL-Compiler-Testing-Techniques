
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, inv_scale_factor=0.125):
        v1  = torch.matmul(q, k.transpose(-2,-1)) 
        v2  = v1 / inv_scale_factor  
        v3  = v2.softmax(dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.5, training=True)
        v5  = v4.matmul(v) 
        return v5

# Initializing the model
m = Model()

 # Inputs to the model
q = torch.randn(8,12,768)
k = torch.randn(8,12,768)
v = torch.randn(8,12,30544)
inv_scale_factor  = 0.125

 # Initializing the model
__output__  = m(q, k, v, inv_scale_factor=inv_scale_factor)