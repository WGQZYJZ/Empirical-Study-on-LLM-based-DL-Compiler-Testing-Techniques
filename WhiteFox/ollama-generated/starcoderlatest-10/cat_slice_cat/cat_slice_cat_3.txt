
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1) # Concatenate input tensors along dimension 1
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(564807, 3, 64, 64)
x2 = torch.randn(9223372036854775807, 3, 64, 64)
