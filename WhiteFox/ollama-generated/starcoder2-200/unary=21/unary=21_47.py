
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
__input_tensor__  = torch.randn(5, 3, 480, 640)
__output__  = m(__input_tensor__)