
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
        self.other  = other
 
    def forward(self, x):
        y = self.linear(x)
        return y + self.other


# Initializing the model
m  = Model()
