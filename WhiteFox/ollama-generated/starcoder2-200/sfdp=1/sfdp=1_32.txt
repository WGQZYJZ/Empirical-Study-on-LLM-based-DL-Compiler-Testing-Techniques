
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.matmul(x1, y)
        v2  = v1 / math.sqrt(8379)
        v3  = torch.nn.functional.dropout(v2, p=0.5)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4863, 10799)
y  = torch.randn(10799, 2048)
__output__  = m(x1)

