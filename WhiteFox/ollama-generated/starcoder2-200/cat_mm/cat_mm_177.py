
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2  = torch.cat([v1] * len([0]))  # Concatenate the result tensor along dimension 4
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
input1  = torch.randn(3, 5)
input2  = torch.randn(3, 8)
__output__   = m(input1, input2)
 
