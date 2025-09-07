
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...)
        v2 = torch.rand_like(v1)
        return v2


# Initializing the model
m = Model()
# Set up graph and register the node for replacement with a lambda function. This is used when `torch.nn.functional.dropout` or `torch.rand_like` are invoked in the `forward` method.
gm.set_node(lambda n: (n.name == 'function') & (n.op.__module__.startswith('aten.')), 1, lambda n: gm.graph.erase_node(n))


# Inputs to the model
x1 = torch.randn(1, 2, 2)
