
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        v = (qk / math.sqrt(float(self.num_attention_heads))) * dropout_p
        a = torch.nn.functional.softmax(v, dim=-1)
        c = dropout_p * a.matmul(x2)
        h = self.conv1(c)
        o = self.conv2(h)
        return o


# Initializing the model
m  = Model()
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(3, 64, 64)
