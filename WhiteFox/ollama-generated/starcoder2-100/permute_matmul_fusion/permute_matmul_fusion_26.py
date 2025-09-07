
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # The inputs' number can be arbitrary (greater than one).
        t1 = x1.permute(0, 3) 
        t1 = torch.bmm(x1, t1) # The tensor methods are different here to simulate a more general case
        return t1

# Initializing the model
m  = Model()

# Inputs to the model (The input numbers should be arbitrary (greater than one).)
x1 = torch.randn(3, 4096, 256, 7) # x1 is of shape [3, 4096, 256, 7].
x2 = torch.randn(256, 4096)       # x2 is of shape [256, 4096]..
