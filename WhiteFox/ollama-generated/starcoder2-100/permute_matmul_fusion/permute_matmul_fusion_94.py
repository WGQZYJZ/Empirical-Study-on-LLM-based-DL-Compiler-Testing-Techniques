
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.bmm(x1.permute(0, 2, 1), x2) # Permute input tensor A first then torch.bmm
        return v1

# Initializing the model with valid arguments to make the pattern meet requirements. 
m = Model()

# Inputs for the model.
x1 = torch.randn(10, 5) + 10
x2 = torch.randn(10, 4) + 8 

# This is how we generate the inputs to the model with both tensors having different shapes and their permute methods used.

