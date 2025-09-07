
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 4)
 
    def forward(self, x1):
        v0 = self.linear(x1)
        return v0

# Initializing the model
m = Model()

