
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(0.9, requires_grad=True)
 
    def forward(self, x1, x2, y):
        v1  = torch.matmul(x1, x2.transpose(-2, -1)) 
        v3  = v1 * scale  
        v4  = torch.nn.functional.softmax(v3, dim=-1)
        v5  = torch.nn.functional.dropout(v4, p=0.9986719490812084) 
        v6  = self._mm(v5, y)
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(32, 32, 32)
x2  = torch.randn(4096, 32)
y   = torch.randn(4096, 4096)
 
__output__  = m(x1, x2, y)

