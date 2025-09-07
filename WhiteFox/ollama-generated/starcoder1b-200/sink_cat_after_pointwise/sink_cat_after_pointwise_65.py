
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Only call this function if you need to call `super()`.
        return x2 + super().forward(x1)  # Forward the input tensor through the model


# Initializing the model
m = Model()


