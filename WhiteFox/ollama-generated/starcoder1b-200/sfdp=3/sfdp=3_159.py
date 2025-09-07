
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 16, 1, stride=1)
        self.key_conv   = torch.nn.Conv2d(3, 16, 1, stride=1)
        self.value_conv  = torch.nn.Conv2d(16, 16, 1)
 
    def forward(self, x1, x2):
        q = self.query_conv(x1)
        k = self.key_conv(x2)
        v = self.value_conv(x2)
        return torch.matmul(q, k.transpose(-2, -1)) * v


# Initializing the model
m  = Model()

