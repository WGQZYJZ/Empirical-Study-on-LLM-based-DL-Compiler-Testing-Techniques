
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * torch.ones([v1.shape[0], 4, 3, 3]) 
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 1, 20, 80) # [batch_size, channels, height, width]
