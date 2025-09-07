
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v3 = v1 + v2 
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8,5)
__x1__  = x1
__x1__ = torch.tensor([[0.947673, -0.399833], [2.843270,-0.333068]]) # This is the input to the first matrix multiplication that is not part of the original model
x2  = torch.randn(5,1)
__x2__  = x2
__x2__  = torch.tensor([[-0.437219],[-1.668595],[0.345088],[2.155216],[1.136699]]) # This is the input to the first matrix multiplication that is not part of the original model
x3  = torch.randn(7,4)
__x3__ = x3
x4  = torch.randn(4,8)
__x4__ = x4


# Initializing a list of inputs and outputs to the model
inputs  = [__x1__, __x2__, __x3__, __x4__] # This is the list of inputs for which we want to obtain the outputs. The order in which they are provided should not be changed here, otherwise your answer may not match with that of the official one
outputs = []


__outputs__  = m(*inputs)