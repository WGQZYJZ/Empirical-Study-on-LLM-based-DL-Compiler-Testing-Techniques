
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = self.linear(x1)  # Pass through the linear transformation
        v2 = v1.permute(0, 2, 1) # Permute the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()

