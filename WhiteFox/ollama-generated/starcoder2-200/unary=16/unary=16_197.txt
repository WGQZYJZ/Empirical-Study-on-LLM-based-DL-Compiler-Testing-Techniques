
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc  = torch.nn.Linear(1024, 6)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v2  = torch.relu(v1)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32, 1024)
__output__  = m(x1)