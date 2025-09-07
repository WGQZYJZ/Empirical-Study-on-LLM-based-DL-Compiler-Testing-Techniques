
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + v6
        v3 = relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(4, 512, 7, 7)
