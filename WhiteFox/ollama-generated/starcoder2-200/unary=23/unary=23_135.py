
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Input size = (N, 3)
        t1 = self.conv2d(x1)  # Output size = (N, 8)
        t2 = torch.tanh(t1)  # Output size = (N, 8)
        return t2


# Initializing the model
m = Model()
__output__  = m(__input__)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -