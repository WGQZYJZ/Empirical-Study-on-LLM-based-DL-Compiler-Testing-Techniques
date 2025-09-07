
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v5  = torch.matmul(x1, y2) 
        v7  = torch.div(v5, inv_scale_factor) # Scale the dot product by the inverse scale factor
        v8  = v7.softmax(-1)                   # Apply softmax to the scaled dot product
        v9  = dropout(v8)                      # Apply dropout to the softmax output
        v10 = torch.mm(x2, v3)                 # Compute the dot product of the dropout output and a value
        return v6


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(8, 5947088)        x2  = torch.rand(5947088, 5387886)     y2  = torch.rand(5387886,)        
__output__  = m(x1, y2)