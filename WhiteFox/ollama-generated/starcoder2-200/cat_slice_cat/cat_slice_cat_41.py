
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t0):
        v1 = torch.cat([t0[:, 2:5], t0[:, 7:9]], dim=1)
        v2 = v1[v1 > 0]
        return len(v2)


# Initializing the model
m  = Model()

# Inputs to the model
t0_dim0 = torch.tensor([[[5,6,3],[4,-9708392178213947874989, -0.], [9333322333799, 5465478, -343]]])
t0_dim1 = torch.tensor([[5], [-9708392178213947874989], [9333322333799]])
__output__  = m(t0_dim0)

