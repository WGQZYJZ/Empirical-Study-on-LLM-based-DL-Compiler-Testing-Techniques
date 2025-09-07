
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1)
 
    def forward(self, x):
        # Perform the two input convolutions
        v1 = self.conv1(x)  # [B, C, H_in, W_in]
        v2 = self.conv2(v1)  # [B, 4, H_out - H_in + 1, W_out - W_in + 1]
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
