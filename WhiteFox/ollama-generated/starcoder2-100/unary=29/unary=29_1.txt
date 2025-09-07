
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn([32], dtype=torch.int64)
        v1  = v0
        v2  = self.conv_transpose(v1)
        v3  = v2.clamp_min(-80) 
        v4  = v3.clamp_max(80)
        return v4
 
