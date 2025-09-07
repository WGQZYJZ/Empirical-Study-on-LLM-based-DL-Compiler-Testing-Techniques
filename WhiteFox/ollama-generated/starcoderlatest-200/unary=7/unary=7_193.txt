
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1) * nn.functional.selu(v1 + 3, inplace=True) / 6
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 128, 40, 40)
