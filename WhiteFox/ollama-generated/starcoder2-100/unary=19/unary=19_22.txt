
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32*8*8, 5)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        return torch.sigmoid(v1)

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(32, 8*8*3)
__output__  = m(x1)

