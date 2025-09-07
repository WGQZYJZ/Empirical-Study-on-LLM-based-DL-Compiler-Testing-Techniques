
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.sigmoid(v1)
        v3 = v1 * v2 # This will fail the test as the order of multiplication is wrong (this is a pattern for gating mechanism).
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4, 2048)
__output__  = m(x1)

