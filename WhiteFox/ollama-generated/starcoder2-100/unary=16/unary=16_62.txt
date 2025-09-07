
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1  = torch.nn.Linear(320, 5)
 
    def forward(self, x1):
        v1  = self.lin1(x1)
        v2  = F.relu(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4096, 320)
__output__  = m(x1)

