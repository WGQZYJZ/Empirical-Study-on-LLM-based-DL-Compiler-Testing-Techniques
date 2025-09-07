
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        qk = torch.matmul(v1, v2.transpose(-2, -1))
        sqk = qk / math.sqrt(math.pi * v1.shape[1] * v2.shape[0])
        s = sqk.softmax(-1)
        o = s * torch.matmul(sqk, x1)
        o = torch.nn.functional.dropout(o, p=dropout_p)
        return o


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
