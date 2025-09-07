
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0 = torch.mm(x1, x2)  # matrix multiplication on two input tensors
        return v0 + 3


# Initializing the model
m = Model()

