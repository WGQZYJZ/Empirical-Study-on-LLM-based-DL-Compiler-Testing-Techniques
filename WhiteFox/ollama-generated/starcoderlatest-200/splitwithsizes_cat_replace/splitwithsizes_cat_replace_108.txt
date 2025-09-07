
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [8], dim=1) # Split tensor along channel axis
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=1) # Concatenate the split tensors along the same dimension
        return v2


# Initialization of the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
