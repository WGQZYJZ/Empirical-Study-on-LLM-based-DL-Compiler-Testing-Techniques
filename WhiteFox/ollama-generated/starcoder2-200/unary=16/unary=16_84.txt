
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc  = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v3  = F.relu(v1) + 1
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x2  = torch.randn(64, 7*7*64)
__output__  = m(x2)

