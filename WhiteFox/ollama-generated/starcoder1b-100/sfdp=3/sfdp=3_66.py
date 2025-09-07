
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        vq = torch.matmul(x1, x2.transpose(-2, -1))
        vm = torch.softmax(vq, dim=-1)
        vd = torch.dropout(vm, p=dropout_p)
        vs = vd.matmul(x2)
        return vs


# Initializing the model
m = Model()

