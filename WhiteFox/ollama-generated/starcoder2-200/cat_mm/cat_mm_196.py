
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v1 = torch.mm(x1, y1) # Matrix multiplication of two input tensors
        v2  = torch.cat([v1] * 5 + [v1], dim=0) 
        return v2
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 64, 3)
y1 = torch.randn(3, 8, 9)

__output__  = m(x1, y1)

# Output tensor from the model.

The resulting tensors have the following shape:

1. When the length of list in `torch.cat` is 5 (default), the output shape is `(4 * 8, 3)` (`* 5 + [v1]`)
2. When the length of list in `torch.cat` is 7 and the dimension to concatenate along is 0, then the output has shape: `(96, 3)`

