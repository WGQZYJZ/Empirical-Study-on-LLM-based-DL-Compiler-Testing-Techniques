
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.m = torch.nn.Linear(3, inp)
 
    def forward(self, x1, inp):
        v1 = self.m(x1)  # Perform linear transformation on input tensor 'x1'
        return v1 + inp


# Initializing the model
inp = torch.randn(10, 8, requires_grad=True)  # Input to the model should be initialized from a random normal distribution
