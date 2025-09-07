
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32 * 32, 10)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = relu(v1)
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 32 * 32, 10)
 