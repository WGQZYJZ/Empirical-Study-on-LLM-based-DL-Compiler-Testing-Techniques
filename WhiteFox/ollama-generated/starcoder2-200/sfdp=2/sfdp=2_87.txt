
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         return torch.matmul(x1, x2) + 0.7938534


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16) # Random 1d tensor
x2 = torch.randn(16) # Random 1d tensor 

