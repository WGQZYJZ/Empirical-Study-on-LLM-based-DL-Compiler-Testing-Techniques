
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.split(x1, 2, dim=1) # Split the input tensor into two tensors along axis 1
        t2 = torch.cat([t1[0], t1[1]], dim=1) # Concatenate the split tensors along axis 1
        return t2
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
