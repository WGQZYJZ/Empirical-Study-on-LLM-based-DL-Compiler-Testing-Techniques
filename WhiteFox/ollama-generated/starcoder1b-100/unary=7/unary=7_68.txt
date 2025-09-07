
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
 
    def forward(self, x):
        return self.linear1(x + torch.clamp(0, 6, x + 3))


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 2, 10)
