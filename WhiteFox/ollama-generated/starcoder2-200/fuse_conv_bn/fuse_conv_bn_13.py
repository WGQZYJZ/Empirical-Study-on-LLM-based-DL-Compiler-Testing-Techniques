
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,  8, kernel_size=3)
        self.bn1  = torch.nn.BatchNorm2d(8)

    def forward(self, x): 
        y1 = self.conv(x)  # Fused
        y2 = self.bn1(y1) # Removed
        return y2

# Initializing the model
m  = Model()
__output__  = m(input_tensor)
