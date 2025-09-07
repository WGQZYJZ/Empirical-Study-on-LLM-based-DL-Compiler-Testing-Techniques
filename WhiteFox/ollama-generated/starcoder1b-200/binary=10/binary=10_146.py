
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 16)
 
    def forward(self, x):
        v1 = self.linear(x) + 5
        return v1


# Inputs to the model
x1 = torch.randn(4, 320)
