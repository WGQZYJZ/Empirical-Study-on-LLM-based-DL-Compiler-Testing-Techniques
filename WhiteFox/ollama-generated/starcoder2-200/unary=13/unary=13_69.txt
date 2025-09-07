
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 8, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = F.sigmoid(v1)
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(8, 512, 8)
__output__  = m(x)


