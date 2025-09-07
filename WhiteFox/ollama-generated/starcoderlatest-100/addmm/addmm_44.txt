
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(input1, input2) # Apply matrix multiplication on two input tensors
        v2 = v1 + 0.5 # Multiply the result of the matrix multiplication by 0.7071067811865476 to produce a new tensor
    return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3)
x2 = torch.randn(10, 3)
