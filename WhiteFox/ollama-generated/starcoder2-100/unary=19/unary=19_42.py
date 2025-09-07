
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32 * 64 ** 2, 1)

    def forward(self, x1):
        v1 = self.fc(x1)
        return torch.sigmoid(v1).flatten()
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(8 * 32 ** 2)
 
__output__  = m(x1)