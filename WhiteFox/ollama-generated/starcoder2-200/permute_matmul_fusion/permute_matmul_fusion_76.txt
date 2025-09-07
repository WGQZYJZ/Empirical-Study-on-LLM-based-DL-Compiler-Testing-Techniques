
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        return torch.bmm(
            x1.permute((0, 2, 3)), # swaps the first and last dimensions of this tensor 
            x2.permute((0, 4, 5)) # swaps the middle two dimensions 
        )


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 6) 
__output__= m(x1, x2)