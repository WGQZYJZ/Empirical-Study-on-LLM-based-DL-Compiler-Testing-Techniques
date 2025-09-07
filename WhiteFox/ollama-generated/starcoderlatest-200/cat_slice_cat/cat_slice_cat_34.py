
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1[:, :9223372036854775807], x1[:, 9223372036854775808:]], dim=1)
        return v1
