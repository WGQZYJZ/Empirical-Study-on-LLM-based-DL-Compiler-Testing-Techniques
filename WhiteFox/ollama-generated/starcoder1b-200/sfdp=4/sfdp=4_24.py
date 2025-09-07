
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, key, value):
        v1 = self.conv(x1)
        qk = (x1 @ key).transpose(-2, -1) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key  = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
