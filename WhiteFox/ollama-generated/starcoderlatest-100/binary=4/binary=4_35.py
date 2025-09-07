
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(3, 8)
        self.other_tensor = torch.randn(16)
 
    def forward(self, x):
        v1 = self.lin1(x)
        v2 = v1 + self.other_tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(8, 3, 64, 64)
