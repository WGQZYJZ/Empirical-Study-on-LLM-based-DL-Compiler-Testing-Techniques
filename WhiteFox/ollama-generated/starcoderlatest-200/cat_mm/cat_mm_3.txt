
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2 = torch.cat([v1] * 3)  # Concatenation of the result tensor along a specified dimension
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_list  = [torch.randn(1, 8), torch.randn(1, 8)]
