
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        qk = (v1 @ x2).div_(math.sqrt(x1.size(-1))).unsqueeze(-1)
        attn_weight = torch.softmax(qk, dim=-1)
        return (attn_weight @ v2).mul(x2)

# Initializing the model
m = Model()


