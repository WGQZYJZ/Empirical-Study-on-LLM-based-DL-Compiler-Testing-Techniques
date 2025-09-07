
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, 2, dim=1) # Split the input tensor into two tensors along the second dimension
        c1 = torch.cat([s1[i] for i in range(len(s1))], dim=1) # Concatenate the split tensors along the same dimension
        return c1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
