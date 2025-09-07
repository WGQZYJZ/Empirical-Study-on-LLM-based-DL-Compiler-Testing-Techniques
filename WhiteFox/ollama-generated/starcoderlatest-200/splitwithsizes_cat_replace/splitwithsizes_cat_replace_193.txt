
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.split(x1, [2, 2, 2], dim=0) # Split the input tensor into three tensors along the batch dimension 
        v2 = torch.cat([v1[i] for i in range(len(v1))]) # Concatenate all split tensors along the batch dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 5, 64, 64)
x3  = torch.randn(1, 8, 64, 64)
