
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1 = self.conv(x1 + other)
        return v1

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8, 256)
