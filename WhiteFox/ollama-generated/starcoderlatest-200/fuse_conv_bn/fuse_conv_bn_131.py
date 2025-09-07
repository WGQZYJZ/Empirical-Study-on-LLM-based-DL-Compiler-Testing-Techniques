
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)

    def forward(self, x1):
        return F.batch_norm(F.conv2d(x1))
    

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 5, 6)
