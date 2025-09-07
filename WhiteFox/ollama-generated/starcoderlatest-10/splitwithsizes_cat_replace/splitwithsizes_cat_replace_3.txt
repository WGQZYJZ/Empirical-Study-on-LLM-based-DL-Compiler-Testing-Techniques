
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, [4], dim=0)  # Split x1 into two tensors along the first dimension using torch.split 
        c1 = torch.cat([s1[i] for i in range(len(s1))], dim=0)  # Concatenate the split tensors along the same dimension
        return c1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
