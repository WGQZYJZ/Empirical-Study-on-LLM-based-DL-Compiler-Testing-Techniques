
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear(v1)
        return torch.matmul(x2, v2).permute(0, 2, 1)

# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(2, 4, 3)
 x2 = torch.randn(1, 2, 3)
 