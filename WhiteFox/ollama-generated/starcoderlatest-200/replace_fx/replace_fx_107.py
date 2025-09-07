
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(p=0.5, inplace=False)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, training=False)  # Dropout for validation set
        v2 = torch.rand_like(v1, requires_grad=True) # Generate a random tensor with the same size as v1 filled with random numbers
        return v2


# Inputs to the model
x1 = torch.randn(10, 48, 48, 3)
