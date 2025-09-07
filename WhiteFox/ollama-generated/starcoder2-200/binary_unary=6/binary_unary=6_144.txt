
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 512)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = F.relu(v2)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(5, 3)

 # Actual input value of 'other'
other  = torch.randn(5, 4)

 # Output from the model with the actual inputs and outputs
__output__  = m(x1)