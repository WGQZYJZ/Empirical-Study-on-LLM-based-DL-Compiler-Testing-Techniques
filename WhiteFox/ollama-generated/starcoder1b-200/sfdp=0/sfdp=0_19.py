
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        x = self.conv(x1)
        sdp = torch.matmul(x, x.transpose(-2, -1)) / torch.sqrt(torch.Tensor([[x.size(-1)], [1]]))
        w = sdp.softmax(dim=-1)
        y = w.matmul(x)

        return y


# Initializing the model
m = Model()


