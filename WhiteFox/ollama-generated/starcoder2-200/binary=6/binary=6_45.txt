
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8*3*4, 1)

    def forward(self, x1):
        v1 = linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 - other # Subtract 'other' from the output of the linear transformation

        return v2


# Initializing the model