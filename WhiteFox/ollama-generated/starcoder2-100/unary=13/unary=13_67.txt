
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model and inputs to it:
m = Model()
x1 = torch.randn(1, 512)
