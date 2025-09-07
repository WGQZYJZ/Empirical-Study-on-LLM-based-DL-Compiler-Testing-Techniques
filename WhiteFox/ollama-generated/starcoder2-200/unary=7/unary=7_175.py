
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
 
    def forward(self, x2):
        y1  = self.linear1(x2) 
        y2  = torch.clamp(y1 + 3 ,min=0, max=6)
        y3  = torch.relu(-y2+9)
        return y3

# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn(5, 3)
__output__  = m(x2)

