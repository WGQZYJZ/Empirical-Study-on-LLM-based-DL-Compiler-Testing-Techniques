
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 8)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0
        v3  = -0.7 * (v1 + 5e-4)
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(100, 8) # batch size is 100 and number of features is 8
__output__  = m(x1)

