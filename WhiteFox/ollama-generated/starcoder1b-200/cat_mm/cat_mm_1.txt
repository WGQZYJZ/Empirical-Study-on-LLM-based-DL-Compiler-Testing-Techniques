
class Model(torch.nn.Module):
    def __init__(self, layer_sizes, dim1=2, dim2=4):
        super().__init__()
        self.layers = torch.nn.Sequential(*[torch.nn.Linear(dim1 if x != dim1 else layer_sizes[x], layer_sizes[x + 1]) for x in range(len(layer_sizes) - 1)])

    def forward(self, inputs):
        v = self.layers(inputs)
        return v


# Initializing the model
m = Model([32, 32, 8], dim1=3, dim2=4)
