
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - 42
        v3  = F.relu(v2)

# Initializing the model
m  = Model()

 # Inputs to the model
__input_tensor__  = torch.randn(1, 3, 64, 64)
 
# Outputs of the model for given input tensor:
__output__  = m(__input_tensor__)

