
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp1):
        v1 = torch.mm(x1, inp1)
        v2 = v1 + inp1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # The first input tensor has shape (1, 3, 64, 64)
inp1 = torch.randn(100000, 8)    # The second input tensor has shape (100000, 8).
