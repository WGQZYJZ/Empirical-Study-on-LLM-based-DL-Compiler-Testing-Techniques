
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64 * 64, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1.reshape(-1))
        v2 = v1 + another_tensor
        v3 = torch.nn.ReLU()(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8 * 64 * 64)
another_tensor = torch.randn(512)
