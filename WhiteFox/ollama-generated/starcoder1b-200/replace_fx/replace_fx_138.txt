
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @torch.jit.script_method
    def forward(self, x1):
        # Original node invoking the function has been erased from the graph with a call to gm.graph.erase_node(node)
        x2 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(x2)  # Generate a tensor of the same size as x2 filled with random numbers
        return v2


# Initializing the model
m = Model()

