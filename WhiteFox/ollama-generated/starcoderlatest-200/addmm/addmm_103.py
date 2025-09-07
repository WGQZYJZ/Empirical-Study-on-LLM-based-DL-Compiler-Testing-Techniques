
class Model(torch.nn.Module):
    def __init__(self, inp=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Perform matrix multiplication on two input tensors
        v2 = v1 + inp
        return v2


# Initializing the model with a value
m = Model()
m = Model(0.5)
m = Model(0)
