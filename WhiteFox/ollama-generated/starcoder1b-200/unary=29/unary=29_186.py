
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-7, max_value=1 - 1e-7):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=(4, 4), stride=(2, 2))
        self.clamp_min = torch.nn.Parameter(torch.tensor(min_value).float())
        self.clamp_max = torch.nn.Parameter(torch.tensor(max_value).float())
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.clamp_min)
        v3 = torch.clamp_max(v2, self.clamp_max)
        return v3


# Initializing the model
m = Model()

