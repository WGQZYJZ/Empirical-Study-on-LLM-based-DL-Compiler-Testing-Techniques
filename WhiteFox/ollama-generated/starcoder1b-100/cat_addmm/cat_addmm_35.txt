
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(1, 8)
        self.fc2 = torch.nn.Linear(8, 1)
 
    def forward(self, x):
        v  = torch.addmm(x, torch.randn(4), torch.randn(4))
        return v


# Initializing the model
m = Model()


