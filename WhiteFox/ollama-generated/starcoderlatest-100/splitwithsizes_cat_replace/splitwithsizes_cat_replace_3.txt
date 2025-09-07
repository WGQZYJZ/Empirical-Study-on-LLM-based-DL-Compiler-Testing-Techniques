
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, [4, 5, 6], dim=3) # Split a 70x20 tensor along the third dimension
        c1 = torch.cat([s1[i] for i in range(len(s1))]) # Concatenate the split tensors along the same dimension
        return c1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 70) # Split this 70x20 tensor along the third dimension
