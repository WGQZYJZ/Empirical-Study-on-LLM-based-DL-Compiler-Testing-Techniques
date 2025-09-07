
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2) # The 1st input tensor is multiplied by the 2nd input tensor and a bias vector is added to it, which results in v1
        v2 = v1 + self.bias # Add the result of the multiplication operation on two tensors to another bias vector, which results in v2
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 5)
__output__  = m(x1)

