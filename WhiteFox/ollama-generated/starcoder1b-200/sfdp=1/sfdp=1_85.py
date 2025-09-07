
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x2.transpose(-2, -1))
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(2, 5, 64, 64)
key    = torch.randn(3, 7, 64, 64)
__output__  = m(query, key)


