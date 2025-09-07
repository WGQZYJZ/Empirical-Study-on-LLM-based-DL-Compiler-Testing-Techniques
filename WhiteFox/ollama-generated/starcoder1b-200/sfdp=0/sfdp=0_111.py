
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # The query tensor has the shape (batch_size, time_step, feature)
        # We can compute attention weights directly if the input is in NCHW format.
        # However, in some applications, inputs are usually in NHWC format so we transpose it here.
        w = torch.matmul(x2.transpose(-2, -1), x1).squeeze()
        inv_scale = torch.sqrt(torch.max(torch.sum((w**2), dim=0) + 1e-15, dim=-1)[0]) * self.dpr[0]  # The dimension of this input is 4*feature.

        return w * inv_scale


# Initializing the model
m = Model()


