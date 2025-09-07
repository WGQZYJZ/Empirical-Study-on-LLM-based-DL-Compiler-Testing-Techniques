
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(2048, 512)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.layer(x1)
        return self.relu(v1)


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(32, 512).float()
__output__= m(x1)


