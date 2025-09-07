
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        return torch.where(x1 > 0, x1 * -2, x1) * 4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
