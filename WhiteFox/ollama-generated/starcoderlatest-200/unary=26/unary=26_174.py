
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=2, padding=0)
        self.negative_slope = torch.nn.Parameter(-torch.ones([]))
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        mask = v1 > 0
        v2 = v1 * self.negative_slope
        where_op = torch.where(mask, v1, v2)
        return where_op

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
