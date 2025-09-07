
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.linear(x1, ...)  # Apply linear transformation to the input tensor.
        return t1.permute(...)  # Permute the output tensor from the linear transformation.


# Initializing the model
m = Model()


