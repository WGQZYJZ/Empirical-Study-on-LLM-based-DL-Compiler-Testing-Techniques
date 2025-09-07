
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.split(x1, [64], dim=2)
        v5  = torch.cat([v0[i] for i in range(3)], dim=2)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 96, 84) # Shape of this tensor depends on the values specified by the user for split_sizes in the optimization, and the total size of input_tensor


