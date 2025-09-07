
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.conv(x)
        v5  = v1 + 174
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
x2  = torch.randn(308396, 8, 128, 128)
