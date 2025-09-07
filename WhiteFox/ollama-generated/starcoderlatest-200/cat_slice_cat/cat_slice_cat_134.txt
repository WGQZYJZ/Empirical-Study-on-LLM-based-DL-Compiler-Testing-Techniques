
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.cat([x1[0:9223372036854775807], x1[:]], dim=1) # Slice the concatenated tensor along dimension 1
        v1 = self.conv(t1)
        return v1


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
