
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 + 1e-6 # added constant 1e-6 to avoid dividing by zero in PyTorch
        return v3


# Initializing the model
m  = Model()


