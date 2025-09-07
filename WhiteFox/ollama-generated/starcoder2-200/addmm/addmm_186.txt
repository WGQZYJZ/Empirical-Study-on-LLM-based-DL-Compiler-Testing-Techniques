
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2) 
        v2 = v1 + inp # The 'inp' argument is used to pass a tensor as an input to the model, this should be different from the previous input tensor.
        return v2
# Initializing the model 
m  = Model()


# Inputs to the model
__input_x1__, __input_x2__, __input_inp1__  = torch.randn(3, 5), torch.randn(4, 6) # Input tensors that should be passed to the model along with the keyword argument 'inp' in 'forward' method.
__output__  = m(__input_x1__, __input_x2__, inp=__input_inp1__)

