
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.3, inplace=True)
        v2 = torch.rand_like(x1, dtype=torch.float)
        return v1 + v2


# Initializing the model and enabling lowmem_ops optimization
m  = Model()
gm = torchani.models.GATModel(
    m,
    cutoffs=(5,),
    num_heads=[8],
    dropout=0.1,
    activation=torch.nn.Tanh,
    device='cpu',
    fallback_random=True,
    lowmem_ops=True,
)


# Inputs to the model
x = torchani.utils.make_graph(gm, x1)[0]

