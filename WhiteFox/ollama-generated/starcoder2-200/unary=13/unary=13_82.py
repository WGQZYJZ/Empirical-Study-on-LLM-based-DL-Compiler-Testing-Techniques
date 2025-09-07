
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128*3, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3049, 8, 64*64*3)
__output__  = m(x1).reshape(-1, 4))