
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v1  = torch.full([x1 + y1, 3], 1)
        v2  = v1.float() # Convert the elements of the tensor to `torch.float64` type 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model