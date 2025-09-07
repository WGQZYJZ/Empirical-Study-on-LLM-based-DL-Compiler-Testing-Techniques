
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        m  = torch.cat([torch.ones((x.shape[0], 1, 1), dtype=x.dtype, device=x.device),
                        -1. * torch.ones((x.shape[0], x.shape[2] + 1, x.shape[3] + 1),
                                            dtype=x.dtype, device=x.device),
                        torch.zeros((x.shape[0], x.shape[2] + 1, x.shape[3] + 1),
                                       dtype=x.dtype, device=x.device)], dim=1)
        v = self.conv_transpose(m * x) / self.negative_slope
        return v


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
