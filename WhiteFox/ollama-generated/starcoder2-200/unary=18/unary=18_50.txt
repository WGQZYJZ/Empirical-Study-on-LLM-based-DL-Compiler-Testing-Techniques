
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.sigmoid(x1) # apply sigmoid function on input tensor
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3072,)
