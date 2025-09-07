
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(16, 8)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        v  = self.linear(x)
        v  = self.sigmoid(v)
        return v


# Initializing the model
m = Model()


