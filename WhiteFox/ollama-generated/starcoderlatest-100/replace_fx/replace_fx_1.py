
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        v = torch.nn.functional.dropout(x, p=0.1, inplace=True)
        v1 = torch.rand_like(v) # Replace the nodes invoking torch.nn.functional.dropout with their corresponding replacement (lowmem_dropout). Afterwards, the node invoking torch.rand_like remains in the graph and triggers gm.graph.erase_node(node) to remove it from the computation graph.
        self.