
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(t1.shape[0] * 2)
        t3 = torch.relu(t2)
        return t3


# Initializing the model and input tensors
m = Model()
x1 = torch.randn(4, 5, 6)
x2 = torch.randn(8, 7, 6)
