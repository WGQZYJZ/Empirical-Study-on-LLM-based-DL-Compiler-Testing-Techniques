
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2560, 3, 97, 97)
x2  = torch.randn(8, 4) # Here x2 is a random tensor, not specified by users but used as an input in the matrix multiplication operation that follows
