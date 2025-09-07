
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v2 = torch.mm(x1, inp) # Perform matrix multiplication on two input tensors and the 'inp' tensor passed as a keyword argument
        v3  = v2 + inp
        return v3


# Initializing the model
m = Model()


# Inputs to the model
__input1__ = torch.randn(64, 50) # Input 1 for the first matrix multiplication operation
inp_tensor=torch.randn(50, 512)   # 'inp' tensor which will be passed as a keyword argument when initializing the model
x2=m(__input1__, __inp=inp_tensor__)


## Sample Model Input: 
- input1: (64L, 32L), random values generated from the interval [-5.0; -5.0]
- input2: 64 * 8 * 8 tensor with random values generated in the interval [-5.0; -5.0]. Please generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model.
- inp1 (keyword argument): 64 * 32 tensor with random values generated from the interval [(-7.0; -5.0)]
