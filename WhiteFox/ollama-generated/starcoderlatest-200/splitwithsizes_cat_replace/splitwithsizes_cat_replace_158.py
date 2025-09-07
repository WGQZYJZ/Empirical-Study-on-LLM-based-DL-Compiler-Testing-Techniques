
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, [3], dim=0) # Split input tensor into three tensors along dimension 0
        v = torch.cat([v[i] for i in range(len(v))], dim=0) # Concatenate the split tensors along dimension 0
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 224, 224)
