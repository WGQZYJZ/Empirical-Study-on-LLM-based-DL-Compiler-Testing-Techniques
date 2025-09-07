
class Model(torch.nn.Module):
    def __init__(self, inputSize):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.cat([x1 for i in range(inputSize)], dim=0)
        return v1[:, :size]


# Initializing the model