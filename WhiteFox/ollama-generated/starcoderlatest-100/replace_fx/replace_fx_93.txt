
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.2, training=True, inplace=False)
        return t1


# Initializing the model and setting fallback_random=True
m = Model()
gm = GraphModule(m, autograd=autograd)
gm.graph = gm.fuse_conv_bn(gm.graph)
gm.compile(fallback_random=True)

# Inputs to the model
x1 = torch.randn(1, 2, 3, 4)
