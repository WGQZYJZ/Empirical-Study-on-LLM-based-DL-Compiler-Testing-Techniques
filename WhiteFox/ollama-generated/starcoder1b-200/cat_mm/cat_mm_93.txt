
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        for _ in range(3):  # In case of concatenation along the third dimension
            v = torch.cat([v, v], dim=1)  # Concatenate along the second dimension
        return v


# Initializing the model
m = Model()


