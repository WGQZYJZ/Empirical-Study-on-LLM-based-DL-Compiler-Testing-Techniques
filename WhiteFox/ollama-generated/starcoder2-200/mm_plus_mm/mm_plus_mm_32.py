
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, 0) # This is not a matrix multiplication but it is used to initialize the model
        v2 = v1 + 0
        return v2


# Initializing the model
m = Model()
