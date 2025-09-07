
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = scalefactor
 
    def forward(self, query, key):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v3  = v1.mul_(self.scale)
        v4  = v3.softmax(-1)
        v5  = torch.nn.functional.dropout(v4, p=0.6)
        return v5


# Initializing the model
m = Model()
 
# Input to the model
k = torch.randn(2, 8973)
q = torch.randn(10, 32, k.shape[-1])
__output__  = m(q, k)
 
