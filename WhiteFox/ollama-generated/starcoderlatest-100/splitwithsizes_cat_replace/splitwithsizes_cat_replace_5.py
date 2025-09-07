
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v  = torch.split(x1, [2], dim=0) # Split input tensor into tensors along dimension dim=0 at position index=0 and the same tensor at position index=1
        return torch.cat([v[0], v[0]], dim=0)
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
