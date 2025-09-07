
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.mm(input3, input4)
        v3  = v1 + v2
        return v3
 
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 50) # Initialize x1 as a randomly generated tensor of shape (64, 50)
x2 = torch.randn(50, 30) # Initialize x2 as a randomly generated tensor of shape (50, 30)
 
# Inputs to the model
