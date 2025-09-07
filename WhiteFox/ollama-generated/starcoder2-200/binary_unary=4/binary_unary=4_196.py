
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(1024, 512)
        self.other  = torch.nn.Parameter(torch.rand((512), requires_grad=True))

    def forward(self, x):
        v1  = self.lin(x)
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(4, 512)
 
 