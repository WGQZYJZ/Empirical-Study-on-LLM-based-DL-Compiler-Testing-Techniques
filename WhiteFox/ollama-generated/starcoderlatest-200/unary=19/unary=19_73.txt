
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 256)
 
    def forward(self, x1):
        v1 = self.linear(x1.reshape(-1))
        v2 = torch.sigmoid(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3*64*64)
