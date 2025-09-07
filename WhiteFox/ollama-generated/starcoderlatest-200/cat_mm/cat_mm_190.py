
class Model(torch.nn.Module):
    def __init__(self, input_dim=3, output_dim=8, cat_dim=-1):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_dim, output_dim, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1, ..., v1], cat_dim=cat_dim)
        return v2
