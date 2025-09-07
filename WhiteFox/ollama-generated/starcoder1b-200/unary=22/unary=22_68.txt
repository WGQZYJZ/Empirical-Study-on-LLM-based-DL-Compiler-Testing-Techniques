
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v  = self.linear(x)
        v = torch.tanh(v)
        return v


# Initializing the model
m  = Model()


