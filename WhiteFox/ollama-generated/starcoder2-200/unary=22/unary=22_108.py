
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x):
        v0 = self.linear(x)
        v1 = torch.tanh(v0)
        return v1


# Initializing the model