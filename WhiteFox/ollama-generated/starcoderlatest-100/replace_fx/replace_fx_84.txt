
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...)
        v2 = torch.rand_like(v1) # This line will not trigger the gm.graph.erase_node
        return v2

