
class Model(torch.nn.Module):
    def __init__(self, inp=20):
        super().__init__()
        self.inp = torch.nn.Linear(3, inp)
 
    def forward(self, x1, x2=None):
        v1 = self.inp(x1)  # Perform linear operation on a tensor 'v1'
        if x2 is None:
            v2 = torch.zeros_like(v1)
        else:
            v2 = self.inp(x2)
        return v1 + v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 15) # Input with shape (batch_size, input_size[0], input_size[1])
inp = torch.randn(3)      # Input with shape (batch_size, input_size[2])


