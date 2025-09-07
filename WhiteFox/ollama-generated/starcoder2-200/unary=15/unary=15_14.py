
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.relu(v1) # Use torch.nn.functional.relu as an alias of F.relu. Also, this is not the recommended way to call the ReLU activation function in PyTorch. Please read the following document https://pytorch.org/docs/stable/nn.html#torch-nn-functional-activation-functions
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__   = m(x1)

