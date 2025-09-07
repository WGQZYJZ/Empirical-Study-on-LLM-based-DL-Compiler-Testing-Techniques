
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


# Initializing the model with 'other' as 0.5
m  = Model()
other  = torch.tensor([[0.5]]) 

# Inputs to the model, and output of m
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

