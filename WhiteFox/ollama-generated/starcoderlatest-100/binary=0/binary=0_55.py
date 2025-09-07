
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        return v6


# Initializing the model
m = Model()

# Inputs to the model
other_tensor  = torch.randn(3, 8, 4096, 4096) # random tensor of shape (C, N, H, W), where C is the number of channels in the input data and N is batch size
x1 = torch.randn(1, 3, 64, 64) # random tensor of shape (B, C, H, W), where B is batch size and C is the number of channels in the input data
