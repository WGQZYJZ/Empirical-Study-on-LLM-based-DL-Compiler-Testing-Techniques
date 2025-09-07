
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32 * 32 * 3, 8)
 
    def forward(self, x1):
        v1 = x1.view(-1, 32*32*3)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 32, 32)
