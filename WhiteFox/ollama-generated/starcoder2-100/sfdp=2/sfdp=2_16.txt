
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1)
        v2  = torch.nn.functional.linear(v1, 100)
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 8)
__output__  = m(x1)

