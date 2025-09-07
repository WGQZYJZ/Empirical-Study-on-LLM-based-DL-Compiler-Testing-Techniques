
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other_tensor # other tensor is an initial tensor not added to the output of convolution at runtime. This value must be determined by user
        v3  = torch.relu(v2) 
        return v3

# Initializing the model with the first tensor (x1) and setting other_tensor randomly:
m,  other_tensor = initializeModel()

 # Inputs to the model should be equal to those from the previous task for the sake of simplicity 
 x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

