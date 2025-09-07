
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3*64*64 ,256)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3*64*64, 500, 500) # change here to make it different from the previous model
__output__  = m(x1)

