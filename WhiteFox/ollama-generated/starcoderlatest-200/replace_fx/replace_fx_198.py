
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # This line will be replaced by gm.graph.erase_node() in replace_fx
        v2 = torch.rand_like(v1)                   # This node will not be replaced and thus will not trigger the gm.graph.erase_node(...) call
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
