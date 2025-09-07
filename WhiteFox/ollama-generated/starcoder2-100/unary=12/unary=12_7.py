
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor  = torch.randn(1, 3, 64, 64)
  __output__  = m(input_tensor)

