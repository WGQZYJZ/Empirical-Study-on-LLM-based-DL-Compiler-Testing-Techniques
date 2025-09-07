
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.randn(32)
        v0 =  torch.reshape(v0, (int((np.prod(x1[1].shape))),))
        v1 = torch.abs(v0)
        v1 =  3 * v1
        v2 = 6
        v3 = v1 + v2
        v4 =  np.minimum(v3, v2)
        v5 = np.maximum(v4, v2)
        v6  = torch.div(v5, v2)
