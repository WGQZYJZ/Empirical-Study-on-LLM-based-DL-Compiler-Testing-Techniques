
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ...):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1, 4 * 5)
        v3 = torch.relu(v2)
        return v3


# Initializing the model and adding a pointwise operation on all tensors in the module. The optimization `sink_cat_after_pointwise` is not triggered because the user has not added an unary operation. Hence, there are no pointwise operations left in the network.
m = Model()
x1 = torch.randn(10, 3)
x2 = torch.randn(15, 7)
