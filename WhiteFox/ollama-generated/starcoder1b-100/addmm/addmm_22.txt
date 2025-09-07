
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.inp = inp

    def forward(self, x1, x2=None):
        v = torch.mm(x1, self.inp)  # Perform matrix multiplication on two input tensors
        if x2 is None:  # If there are no inputs for the model's forward method
            return v  # Use 'v' as an output of the method (see comment above)
        else:
            return v + x2  # If any other argument exists, add it to 'v'.


# Initializing the model
m = Model(inp=torch.randn(1, 3, 64, 64))
x1 = torch.randn(1, 3, 64, 64)
