
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1): 
        v1 = self.conv(x1)
        v2  = v1 - other_tensor
        v3  = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1   = torch.randn(1, 3, 64, 64)

 # Adding a tensor or scalar with which to subtract from the output of the convolution
other_tensor = F.relu(x2)

 # Initializing the input tensors in addition to other inputs such as previously defined variables and initializers required by this model 
 x2  = torch.randn(1, 3, 64, 64)
 
 __output__   = m(x1)
