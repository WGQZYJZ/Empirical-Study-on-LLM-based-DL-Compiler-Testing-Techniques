
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1=None, x2=None):
        v1 = torch.mm(x1, x2)
        return v1 + inp


# Initializing the model 
m = Model()

# Inputs to the model 
inp = torch.randn(500) # Tensor to be added to matrix multiplication result
x1 = torch.randn(100, 3)
x2 = torch.randn(3, 60)


__output__  = m(x1=x1, x2=x2)

