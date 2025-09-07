
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x1):
        v  = torch.mm(x1, x1) # Matrix multiplication of two input tensors.
        v2 = torch.cat([v] * 3, dim=0) 
        return v2


# Initializing the model
m = Model(input1, input2)

# Inputs to the model
x1 = torch.randn(5, 4) # Randomly generated tensor with shape (5, 4).
__output__  = m(x1)

