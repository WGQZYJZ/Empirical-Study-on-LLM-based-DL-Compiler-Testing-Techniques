
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        y1 = self.linear(x1)
        return y1


# Initializing the model
m = Model()


# Inputs to the model
inputs = (torch.randn(10), torch.randn(2, 4))
