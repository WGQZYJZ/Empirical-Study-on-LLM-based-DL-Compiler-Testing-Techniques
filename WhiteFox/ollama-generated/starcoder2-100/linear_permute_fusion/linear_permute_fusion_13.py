
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1) # Linear transformation on the input vector.
        v2  = v.permute(0, 3, 1, 2) # Permute output tensor of the linear function to a 4D tensor.
        return v2

# Initializing model