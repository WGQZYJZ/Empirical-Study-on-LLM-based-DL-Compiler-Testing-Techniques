
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1  = torch.matmul(x1, x2) # Dot product of x1 and x2
        v2  = v1 * 0.5              # Scale the dot product by a factor of .5
        v3  = v1.softmax(-1).dropout(p=0.8) # Apply softmax to the scaled dot product, then apply dropout to the output
        return v2


# Initializing the model
m = Model()

# Input tensors to the model
t01 = torch.randn(32, 54769)
t02 = t01
t03 = t01
