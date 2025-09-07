
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *args):
        v1 = torch.cat(args[0], dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, args[1]:] # Slice the concatenated tensor along dimension 1
        return v2


# Initializing the model
m = Model()

# Input tensors to the model. Here we assume that they are already created.
x1 = torch.randn(10, 3)
x2 = torch.randn(5, 4)

# Calling the model with a list of input tensors and an index used in slicing. In this example we call it with an index 0
out = m([x1, x2], 0)

