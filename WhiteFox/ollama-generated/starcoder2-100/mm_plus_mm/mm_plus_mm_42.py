
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v1 = torch.mm(x1[0], x1[2])  # Matrix multiplication between first and third matrix
        v2 = torch.mm(x1[4], x1[5])  # Matrix multiplication between fourth and fifth matrix
        v3 = v1 + v2                 # Addition of the results of the two matrix multiplications
        return v3

# Initializing the model
m  = Model()


# Inputs to the model (two tensors)
x1  = torch.randn(6, 4096), torch.randn(5072) 

# Predicting with the model on the inputs above
__output__  = m(x1)
