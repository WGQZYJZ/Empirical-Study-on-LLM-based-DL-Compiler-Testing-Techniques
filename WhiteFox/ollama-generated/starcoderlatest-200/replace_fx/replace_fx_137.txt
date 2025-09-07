
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1, ...)  # Generate a tensor with the same size as input_tensor filled with random numbers
        ...
        return __output__


# Initializing the model
m = Model()
gm = glow.Glow(model=m, fallback_random=False)


def f(x):
    t1 = torch.nn.functional.dropout(...)  # This will not be replaced by replace_fx and hence trigger `gm.graph.erase_node`
    v2 = torch.rand_like(input_tensor, ...)  # Generate a tensor with the same size as input_tensor filled with random numbers
    return __output__


# Initializing a simple function call graph for model 'm' and function 'f'. The generated Graph is an EquivalenceGraph object, which contains nodes that represent instructions.
gm = glow.Glow(model=m)
gm.add_function(f) # Add f to the Glow instance


# Inputs to the model
x1 = torch.randn(1, 2, 2)
