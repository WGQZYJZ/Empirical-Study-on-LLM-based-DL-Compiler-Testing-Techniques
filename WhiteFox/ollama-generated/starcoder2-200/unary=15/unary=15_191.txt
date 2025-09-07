
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
__input__  = torch.randn(1, 3, 64, 64)
x1 = __input__.clone()
 
# Forward pass with original model
__output_old__ = m(x1)

# Forward pass using new model (which is different from the previous one):
m2 = Model().to(__input__.__device__) # make sure to use the same device as the input tensor (__input__ here).
__output__  = m2(x1)

