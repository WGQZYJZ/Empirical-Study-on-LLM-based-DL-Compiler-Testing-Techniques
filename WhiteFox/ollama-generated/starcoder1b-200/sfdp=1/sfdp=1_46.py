
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x, y):
        query = torch.randn(4, 3, 64, 64)
        key    = torch.randn(5, 3, 64, 64)
        scale  = torch.randn_like(query).div_(1e-7)
        softmax_scale_factor = torch.softmax(scale, dim=-1)
        value  = torch.randn(1, 8, 32, 32)
        scaled_value = value * softmax_scale_factor
        output = self.conv(scaled_value)
        return output
