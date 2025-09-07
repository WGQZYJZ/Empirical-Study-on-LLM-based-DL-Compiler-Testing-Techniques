
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x) 
        v2 = torch.sigmoid(v1) # sigmoid(conv(x)) = torch.sigmoid(conv(x) * 0.5) * 0.7071067811865476 * 0.3989422804014327
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
