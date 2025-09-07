
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2):
        v2 = self.linear(x2)
        v3 = v2 - 0.49999999999999994
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 8)
