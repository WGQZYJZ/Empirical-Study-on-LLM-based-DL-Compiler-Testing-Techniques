
class Model(torch.nn.Module):
    def __init__(self, scale=32768.0):
        super().__init__()
        self.scale = scale
        self.conv  = torch.nn.Conv1d(4, 5, kernel_size=1)

    def forward(self, x1):
        v1  = torch.matmul(x1, 2 * torch.randn((3072))) / (self.scale + torch.norm(x1))
        v2  = self.conv(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(5, 4, 3072).div(60)

 __output__  = m(x1)

