
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2)
# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
 # Initial value of another tensor
other  = 0.5
 
# Feed inputs into the model and capture its output
with torch.no_grad():
    __output__   = m(x1)

