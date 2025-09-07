
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2)
        v2 = torch.mm(v1, v1) # Vectorized version of matrix multiplication
        v3 = torch.mm(v2, v3) # Vectorized version of matrix multiplication
        return v3


# Initializing the model
m  = Model()


