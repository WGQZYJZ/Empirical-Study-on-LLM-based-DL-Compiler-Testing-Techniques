
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 64**2 , 5)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 > 0
        v3  = v1 < 0
        v4  = v3 + negative_slope
        v5  = torch.where(v2, v1, v4)
        return v5

 # Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(784).view(-1 , 1 , 64 , 64)
__output__  = m(x)

