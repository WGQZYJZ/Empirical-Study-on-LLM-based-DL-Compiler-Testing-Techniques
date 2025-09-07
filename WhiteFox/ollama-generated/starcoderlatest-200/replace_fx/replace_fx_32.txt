
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.25)
        t2 = torch.rand_like(x1, 4) # This node is going to be replaced with the lowmem_dropout operator in replace_fx optimization
        return t1 + t2

# Initialize the model and specify which ops are supposed to replace random functions
m = Model()
gm.initialize([
    gm.GraphModule(m, ["forward"], [lambda graph, mod: gm.add_operator(graph, torch_ops.lowmem_dropout, 1), lambda graph, mod: gm.add_operator(graph, torch_ops.rand_like, 2)])
])

# Inputs to the model
x1 = torch.randn(1, 8, 6)
gm.run([gm.GraphModule(m, [x1], [])], "forward", batch_size=1)

