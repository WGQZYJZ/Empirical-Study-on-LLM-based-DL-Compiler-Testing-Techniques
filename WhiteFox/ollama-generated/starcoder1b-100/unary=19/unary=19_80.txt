
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x):
        v = self.linear(x)
        return torch.sigmoid(v)

 # Inputs to the model
 x1 = torch.randn(2, 3)
 