
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = torch.split(x1, [10], dim=1) # Split into 2 tensors along dimension 1
        x3 = torch.cat([x2[i] for i in range(len(x2))], dim=1) # Concatenate along the same dimension
        return x3
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(20, 3, 64, 64)
