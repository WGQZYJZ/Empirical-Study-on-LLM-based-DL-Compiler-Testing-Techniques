
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other # Replace other here with the constant or another tensor that can be inferred by your analysis tool
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1,3,64,64)
