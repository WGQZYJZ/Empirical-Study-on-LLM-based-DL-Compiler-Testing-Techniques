
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.size()[0], -1))
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
