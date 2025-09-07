
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 2)
 
    def forward(self, x):
        v1 = torch.addmm(x, x.new_ones(1, 3), x.new_ones(3, 1))
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(64, 3)
