
class Model(torch.nn.Module):
    def __init__(self, inv_scale=1024)
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = scaled_dot_product = torch.matmul(v1, v1.transpose(-2, -1)) / inv_scale
        v3  = v2.softmax(dim=-1)
        v4  = v3.matmul(v3)
        return v4

# Initializing the model
m = Model()

