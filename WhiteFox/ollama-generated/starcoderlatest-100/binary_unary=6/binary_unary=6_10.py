
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8*24*192, 36864)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.30379177426256267 # Subtraction constant of the desired output
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
