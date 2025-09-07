
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3*64*64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.flatten())
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3*64*64, 50).T # transpose the 2D array of input size (64 * 64 * 3) into a 1D array of length 3 * 64 * 64. We do not pass in a batch dimension here.
