
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 80)
 
    def forward(self, x1):
        return self.linear(x1)


m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
