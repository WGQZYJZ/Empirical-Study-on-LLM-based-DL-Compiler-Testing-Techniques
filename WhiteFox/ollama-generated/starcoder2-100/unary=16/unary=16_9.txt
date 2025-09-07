
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 3)
 
    def forward(self, x1):
        v0 = torch.nn.ReLU()
        return v0(x1)


# Initializing the model
m  = Model()
 

# Inputs to the model
x1  = torch.randn(64, 512)
 
__output__  = m(x1)