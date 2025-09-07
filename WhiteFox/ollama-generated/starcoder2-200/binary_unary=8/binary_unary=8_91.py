
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other_tensor 
        v3  = torch.relu(v2)
        return v3


# Initializing the model with a non-zero other tensor as input to the model and then generating the output of the model
m  = Model()
other  = torch.randn(64, 8, 10) + 10000 # The input tensor should not be constant or 0s (The model will give a different result if it is a 0s or constant tensors)
__output___1  = m(torch.randn(1,3,64,64), other)

