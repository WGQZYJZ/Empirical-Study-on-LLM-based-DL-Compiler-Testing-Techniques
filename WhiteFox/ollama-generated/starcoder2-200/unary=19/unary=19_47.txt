
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3 , 1)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = torch.sigmoid(v1) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64, 3).permute((0, 3, 1, 2))  # permute is used to convert (3, 64, 64, 3) to (3, 3, 64, 64), because Conv2d expects a specific input format.
