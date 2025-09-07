
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(160, 3)
 
    def forward(self, x):
        return self.linear(x) + another

    