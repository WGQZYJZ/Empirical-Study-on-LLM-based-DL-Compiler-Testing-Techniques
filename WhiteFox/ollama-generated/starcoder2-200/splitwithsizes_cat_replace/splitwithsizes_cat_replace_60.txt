
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t  = torch.split(x1, [32], 0) # Splits the input tensor into several tensors along dimension 0. The size of each tensor is equal to 32 elements.
        v  = torch.cat([t[i] for i in range(len(t))], 0) # Concatenates these split tensors along dimension 0.
        return v
# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(64, 320, 5, 5)

