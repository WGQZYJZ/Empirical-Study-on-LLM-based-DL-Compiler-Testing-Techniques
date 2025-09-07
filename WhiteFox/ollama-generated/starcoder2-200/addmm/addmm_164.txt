
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, self._other) + inp

# Initializing the model and passing keyword argument to the forward function of Model class
m = Model()
inp  = torch.randn(320, 58960) # Passing a randomly generated tensor as input_tensor for input1 parameter in the forward function of the Model class


x1 = torch.rand((48, 17)) # Passing a randomly generated tensor as input_tensor for input2 parameter in the forward function of the Model class
__output__  = m(x1, inp)

