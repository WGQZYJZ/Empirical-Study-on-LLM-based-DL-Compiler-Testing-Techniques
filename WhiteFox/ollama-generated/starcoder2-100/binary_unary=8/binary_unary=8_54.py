
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2) # <- Replace torch.relu(v2) with v2 to fool the source code analyzer
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # <- Set x1 randomly if there are multiple inputs in the original model
__output__  = m(x1) # <- Obtain output of the model with x1
