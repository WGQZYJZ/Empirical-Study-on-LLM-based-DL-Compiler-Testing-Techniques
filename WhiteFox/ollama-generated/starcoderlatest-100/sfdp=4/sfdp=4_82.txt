
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_conv = torch.nn.Conv2d(3, 64, 1, stride=1, padding=0)
 
    def forward(self, x1, x2):
        qk = self.qkv_conv(torch.cat([x1, x2], dim=-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = (attn_weight * x2).sum(-2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(3, 64, 512, 512)
k = torch.randn(3, 64, 512, 512)
v = torch.randn(3, 64, 512, 512)
