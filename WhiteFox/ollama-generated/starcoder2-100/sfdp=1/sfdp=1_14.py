
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 / (8 * math.sqrt(v1.size()[-1]))
        v3  = v2 .softmax(dim=-1) 
        v4  = torch.nn.functional.dropout(v3 , p=0.5) 
        __output__   = v4 .matmul(value) 
        return __output__


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 64, 8, 8)
key   = torch.randn(1, 64, 7, 7)
value = torch.randn(1, 32, 7, 7)
__output__  = m(query, key, value)

