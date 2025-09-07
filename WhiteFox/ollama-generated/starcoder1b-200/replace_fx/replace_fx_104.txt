
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Use the `gm.graph.erase_node()` function to erase the original input tensor from the model graph. This way it does not trigger the `gm.graph.erase_node(node)` line.
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()


