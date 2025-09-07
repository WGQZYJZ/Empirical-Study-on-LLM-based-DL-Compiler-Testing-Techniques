

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1) # Apply linear transformation to the input tensor
        return v.permute(0, 2, 1)

# Initializing the model