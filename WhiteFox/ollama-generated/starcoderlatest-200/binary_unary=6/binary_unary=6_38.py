
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3 * 64 * 64, 512, bias=True)
 
    def forward(self, x1):
        v1 = self.conv(x1.view(x1.size(0), -1))
        v2 = v1 - other
        v3 = torch.nn.ReLU()(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
