
class Model(torch.nn.Module):
    def __init__(self, num_layers=1):
        super().__init__()
        self.net = ...  # Initialize sub-modules

    def forward(self, x1):
        outs = []
        for _ in range(num_layers):
            # The output is then reshaped back to the original shape.
            outs.append(...).permute(...)
        return ...


# Initializing the model
m = Model()


