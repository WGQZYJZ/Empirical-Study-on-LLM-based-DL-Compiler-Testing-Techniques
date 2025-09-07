
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5, inplace=True) # replace_fx will replace nn.functional.dropout with lowmem_dropout
        t2 = torch.rand_like(x1) # do not replace this node, because of the CPU fallback configuration
        __output__  = x1
        return __output__


# Initializing the model
m = Model()


