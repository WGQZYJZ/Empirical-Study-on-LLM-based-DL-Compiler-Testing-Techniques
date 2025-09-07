
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(512, 64)
        self.layer2 = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.layer1(x1) # Layer 1: Apply a linear transformation to the input tensor
        v2 = self.layer2(v1) # Layer 2: Apply another linear transformation to the output of layer 1
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 512, 4096)
