
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)
        # If replace_fx is enabled, the `gm.graph.erase_node` will not be called and hence the node invoking the dropout function will still exist in the graph. Hence, it will trigger a 'No matching node found in the pattern' error when executing the model.
        v2 = torch.nn.functional.linear(v1, self.linear.weight)
        return v2

# Initialization
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
