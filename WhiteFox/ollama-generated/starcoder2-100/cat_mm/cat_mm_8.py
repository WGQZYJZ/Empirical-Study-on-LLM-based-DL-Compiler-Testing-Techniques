
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v3  = [v1] * len(v1)
        v4  = torch.cat(v3) # Concatenate the result tensor along a specified dimension
        return v4


# Initializing model
m = Model()
input1  = torch.randn(5, 20, requires_grad=True)
input2  = torch.randn(5, 19, requires_grad=True)
 
# Calling the model
m(input1, input2)

