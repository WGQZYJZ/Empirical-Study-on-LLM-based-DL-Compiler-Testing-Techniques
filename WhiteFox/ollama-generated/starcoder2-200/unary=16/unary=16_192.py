
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(128, 5)
 
    def forward(self, x):
        v0 = self.fc(x)
        v1 = F.relu(v0)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(64, 128)
__output__  = m(x)

