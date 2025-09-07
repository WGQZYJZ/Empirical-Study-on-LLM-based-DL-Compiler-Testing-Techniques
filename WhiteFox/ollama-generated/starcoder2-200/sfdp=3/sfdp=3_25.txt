
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale = 20000

        v1 = torch.matmul(query, key.transpose(-2, -1)) * scale
        v2 = torch.nn.functional.dropout(v1.softmax(dim=-1), p=0.85)
        v3 = v2.matmul(value)
 
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
q, k, v  = [torch.randn(4, 4, 7)] * 3
__output__  = m(q, k, v)

