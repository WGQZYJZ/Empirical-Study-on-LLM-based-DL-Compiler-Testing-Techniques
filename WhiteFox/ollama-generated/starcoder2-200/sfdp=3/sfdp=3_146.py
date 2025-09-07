
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat_mul  = torch.nn.Linear(256, 30)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 * 4
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5)
        v5  = self.mat_mul(v4).matmul(value)
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(16, 256)
key  = torch.randn(16, 30, 256)
value  = torch.randn(16, 30, 8704)
__output__  = m(query, key, value)

