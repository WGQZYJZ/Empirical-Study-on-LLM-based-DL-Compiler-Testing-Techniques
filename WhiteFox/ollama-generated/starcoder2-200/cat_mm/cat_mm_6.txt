
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
        self.mm  = torch.nn.Linear(256*dim**2+108, 9) # Replace dim**4 with dim**2 in the argument of self.mm
        self.cat  = torch.nn.Flatten()
 
    def forward(self, x):
        return self.mm(x).reshape(-1, 3, 64*dim, 64*dim).mean([2, 3]) # Replace dim**2 with 3 in the argument of self.mm


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(108, 9) + torch.zeros((108*dim**4 + 108, )) # Replace dim**2 with 3 in the argument of torch.randn

