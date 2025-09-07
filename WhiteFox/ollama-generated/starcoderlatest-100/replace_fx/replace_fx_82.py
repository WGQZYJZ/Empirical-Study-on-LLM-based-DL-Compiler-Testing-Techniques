
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1)
        v2 = torch.nn.functional.dropout(v1, ...)
        return v2


# Initializing the model and applying replace_fx
m = Model()
torch_graph(m)
torch._C._jit_pass_lowmem_type_elimination_helper(torch_graph(m), torch_fuser_enabled=True)

# Inputs to the model and invoking `gm.replace_op`
x1 = torch.randn(1, 2, 2)
torch._C._jit_pass_lowmem_type_elimination_helper(
    gm.replace_node(gm.graph().create_node('aten::rand', 't0')))

