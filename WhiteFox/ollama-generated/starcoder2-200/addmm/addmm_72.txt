
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp): 
        v1 = torch.mm(x2, x3) # Matrix multiplication operation on two input tensors. 
        return v1 + inp  # Add the result of matrix multiplication to another tensor 'inp'.


# Initializing the model
m  = Model()
