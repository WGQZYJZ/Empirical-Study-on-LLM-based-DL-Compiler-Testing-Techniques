
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Apply matrix multiplication to inputs x1 and x2
        return v3


# Initializing the model
m = Model()


