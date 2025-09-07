
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 48)
        self.linear2 = torch.nn.Linear(48, 32)
 
    def forward(self, x):
        v = self.linear1(x) + self.linear2(x)
        return v

# Initializing the model
m = Model()

