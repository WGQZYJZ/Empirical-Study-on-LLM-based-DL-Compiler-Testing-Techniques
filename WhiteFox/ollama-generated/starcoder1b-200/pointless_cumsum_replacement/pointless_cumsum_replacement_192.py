
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([1], 1, dtype=torch.float32, layout=torch.strided) # Create a tensor filled with the scalar value 1, with the specified dtype and layout (memory location), and device (GPU/CPU).
        return t1 + x2


# Initializing the model
m = Model()


