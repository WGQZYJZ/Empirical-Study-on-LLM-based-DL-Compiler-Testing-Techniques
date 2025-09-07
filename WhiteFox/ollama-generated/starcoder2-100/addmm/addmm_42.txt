
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2) # Matrix multiplication on two tensors
        v2 = v1 + 640 
        return v2


# Initializing the model
m  = Model()
 
# Input to the model
__input_tensor1__  = torch.randn(32, 32) 
__input_tensor2__  = torch.randn(32, 512) 

# Initializing the input tensor 2 as a keyword argument:
m(x1=__input_tensor1__, x2=__input_tensor2__)

