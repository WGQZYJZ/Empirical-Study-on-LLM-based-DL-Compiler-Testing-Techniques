
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate input tensors along dimension 1
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3487659234875348, 17)
x2 = x1 * 0.5 # Generating a tensor that is different from x1 using PyTorch operations
