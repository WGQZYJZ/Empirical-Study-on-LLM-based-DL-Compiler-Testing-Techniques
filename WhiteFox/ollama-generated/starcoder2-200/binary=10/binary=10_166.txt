
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 40)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        return v1 + other
# Initializing the model
m  = Model()

# Inputs to the model
other = torch.randn(32, 89)

x1   = torch.randn(32, 256)
