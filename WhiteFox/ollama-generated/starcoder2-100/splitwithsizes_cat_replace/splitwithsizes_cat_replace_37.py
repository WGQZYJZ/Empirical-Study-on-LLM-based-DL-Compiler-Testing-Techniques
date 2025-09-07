
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = torch.split(x1, 50, dim=3) # Split the input tensor into several tensors along dimension 3 with sizes of 50 each
        y2 = [torch.cat([x2[i]], dim=dim) for i in range(len(x2))] # Concatenate these split tensors back to an original size by specifying its dimension (dimension 1 here as the number of concatenated tensors is always one)
        return torch.cat(y2, dim=3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 3, 64, 70)
__output__  = m(x1)