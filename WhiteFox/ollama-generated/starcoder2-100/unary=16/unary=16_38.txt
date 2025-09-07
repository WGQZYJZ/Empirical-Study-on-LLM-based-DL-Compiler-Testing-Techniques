
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc  = torch.nn.Linear(32000, 1)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v2  = F.relu(v1)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(640,32000)
__output__  = m(x1)
