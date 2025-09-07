
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3,8)

    def forward(self, x1):
         v2  = fc(x1)
         v3  = torch.sigmoid(v2)
         return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(50000, 3)

__output__  = m(x1)

