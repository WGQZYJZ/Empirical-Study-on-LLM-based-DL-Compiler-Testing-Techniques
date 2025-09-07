

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4):
        v0  = torch.mm(input1, input2) # Matrix multiplication between two tensors 
        v1  = torch.mm(input3, input4) # Matrix multiplication between two tensors
        v2  = v0 + v1 # Addition of the results of two matrix multiplications
        return v2


# Initializing the model with randomly generated tensors as inputs.
m  = Model()
v0_random = torch.randn(3, 5)
v1_random = torch.randn(4, 8)
v2_random = torch.randn(5, 9)
