
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 3, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32 * 32 * 3))
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
