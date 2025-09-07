
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3  = torch.relu(x1 + x2)
        return v3


m = Model()
__output__= m(x1_tensor, x2_tensor)
