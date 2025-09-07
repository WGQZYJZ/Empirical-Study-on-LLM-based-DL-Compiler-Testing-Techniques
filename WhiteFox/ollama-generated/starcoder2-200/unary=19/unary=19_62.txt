
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*32*32+50, 1)
 
    def forward(self, x1, x2):
        v1 = torch.flatten(x1, start_dim=1)
        v2 = torch.cat((v1, x2), dim=1)
        v3 = self.linear(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(4096, 32, 32, 5)
x2  = torch.randn(4096, 50)
__output__  = m(x1, x2)

