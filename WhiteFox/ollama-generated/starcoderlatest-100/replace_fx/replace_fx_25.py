
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, self.dropout)
        v2 = torch.rand_like(x1)
        return v2


# Initializing the model and checking if `torch.rand_like` is replaced with `lowmem_rand_like` during compilation
m  = Model()
gm.optimize_graph(m, fallback_random=True)
gm.run([gm.graph.nodes[0]])
gm.run([gm.graph.nodes[1]])
# gm.run will return an error saying that the input is not a tensor because `torch.rand_like` takes a single argument instead of two arguments

