
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2_a = v1 - other() # where other() is another tensor or a scalar value
        v2_b = v1 + torch.randn([])  # where torch.randn(...) is another tensor or a scalar value
        v3   = relu(v2_a) + relu(v2_b)
        return v3
