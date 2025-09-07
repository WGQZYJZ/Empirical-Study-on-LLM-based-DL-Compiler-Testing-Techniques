
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)
 
    def forward(self, x):
        w = self.linear(x)
        return torch.where(w > 0, w, 0.2 * w)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 4)
