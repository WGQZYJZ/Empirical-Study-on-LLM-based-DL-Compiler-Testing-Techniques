
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 10 + 5, 3)
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v9  = torch.randn(8).add_(v7) 
        v14 = torch.relu(-v7 + v9 + other)
        return v14


# Initializing the model
m = Model()

 # Inputs to the model
x3  = torch.randn(2, 5 * 10 + 8)
__output__  = m(x3)

