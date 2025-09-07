
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear()(x1)
        v2  = torch.nn.Sigmoid()(v1)
        return v1 * v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 50)
__output__  = m(x1)


