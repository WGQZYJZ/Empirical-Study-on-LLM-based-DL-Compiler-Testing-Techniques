
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3) # replace the condition
        return v4


# Initializing the model
m = Model()
negative_slope = 5e-3

# Inputs to the model
x1 = torch.randn(10, 2048)

__output__  = m(x1)