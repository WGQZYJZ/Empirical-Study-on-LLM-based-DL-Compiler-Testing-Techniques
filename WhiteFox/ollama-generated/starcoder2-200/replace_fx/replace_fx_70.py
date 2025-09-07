class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # noqa: F811
        torch._replace_random_with_randlike_in_graph(x1)  # Replace torch.nn.functional.dropout with lowmem_dropout and torch.rand_like with rand_like in the graph of this module.
        return
