
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        # If `fallback_random` is set, then the fallback node invoking `torch.rand_like` will not be replaced and thus will not trigger the `gm.graph.erase_node(node)` line. So here we only replace the nodes calling `torch.rand_like`. 
        v2 = self.linear(torch.rand_like(v1))
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
