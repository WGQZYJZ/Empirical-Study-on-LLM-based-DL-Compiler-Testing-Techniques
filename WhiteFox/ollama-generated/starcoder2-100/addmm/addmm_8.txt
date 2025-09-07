
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)  # Matrix multiplication operation on two tensors
        v2 = v1 + inp   # Add the matrix multiplication result to a tensor
        return v2

# Initializing the model
m = Model()
