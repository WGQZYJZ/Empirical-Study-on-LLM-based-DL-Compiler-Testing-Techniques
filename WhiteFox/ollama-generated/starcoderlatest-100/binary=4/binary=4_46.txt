
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.conv = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
