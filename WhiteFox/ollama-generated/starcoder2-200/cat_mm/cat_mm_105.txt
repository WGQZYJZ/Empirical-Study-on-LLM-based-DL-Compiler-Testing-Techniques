
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2) # Matrix multiplication of two input tensors
        v2  = torch.cat([v1 for _ in range(4)], dim=0) # Concatenation of the result tensor along a specified dimension 
        return v2


# Initializing the model
m  = Model()
 

# Inputs to the model