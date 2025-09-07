
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, **kwarg): # Keyword arguments
        v0 = torch.mm(input1, input2)  # Apply matrix multiplication to the two tensors
        v1 = v0 + kwarg["inp"] # Add the result of this operation to another tensor "inp"
        return v1

# Initializing the model
m  = Model()

