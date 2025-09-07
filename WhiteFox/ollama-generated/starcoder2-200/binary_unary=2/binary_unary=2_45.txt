
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
         v0  = self.conv(x1)
         v1  = v0 - 5476
         v2  = F.relu(v1)
         return v2

m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
