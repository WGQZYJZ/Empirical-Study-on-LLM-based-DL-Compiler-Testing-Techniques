
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        v1 = torch.matmul(query, key.transpose(-2,-1))
        v2 = v1 / 8000.0
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.5) 
        return v4


# Initializing the model
m = Model()
 
 # Inputs to the model
query  = torch.randn(8, 96, 2)
key  = torch.randn(8, 96, 2)
__output__  = m(query , key)

