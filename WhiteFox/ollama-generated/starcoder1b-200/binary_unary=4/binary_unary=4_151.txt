
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        return self.linear(x) + other


# Initializing the model
m = Model(torch.tensor([1.]))

