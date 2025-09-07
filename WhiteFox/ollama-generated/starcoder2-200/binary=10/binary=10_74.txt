
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(64*64*3, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1.flatten())
        return v1
 
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(5, 64*64*3)
__output__  = m(x1)


