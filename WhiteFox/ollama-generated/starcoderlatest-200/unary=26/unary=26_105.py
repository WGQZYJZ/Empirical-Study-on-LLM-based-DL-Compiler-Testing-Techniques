
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 > 0).float()
        negative_slope = torch.tensor([0.75]).to('cuda')
        v3 = v1 * negative_slope
        where_func_result = torch.where(v2, x1, v3)
        return where_func_result


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64).to('cuda')
