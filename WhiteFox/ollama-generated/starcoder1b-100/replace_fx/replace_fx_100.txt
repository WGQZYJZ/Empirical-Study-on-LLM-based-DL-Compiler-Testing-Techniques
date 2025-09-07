
class Model(torch.nn.Module):
    def __init__(self, random: bool=True):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        if random:
            # We need a `random_like` function to generate the input tensor with a fixed shape, otherwise the nodes will be erased.
            self.x2 = torch.rand_like(self.linear.weight)

    def forward(self, x1):
        v1 = self.linear(x1)
        if not self._need_random: # `fallback_random` is enabled, or if running on a CPU device
            # Nodes in the graph corresponding to nodes invoking `torch.nn.functional.dropout` are erased, and thus these nodes will not trigger the `gm.graph.erase_node(node)` line.
            v1 = v1.view(-1)
        self._need_random = False
        return v1


# Inputs to the model
x1 = torch.randn(1, 2, 3, 3)
