
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask = (v1 > 0).to(torch.float)

        v3  = v1 * negative_slope
        return torch.where(mask, v1, v3)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

Inputs to the model:
- input_tensor: torch.Size([1, 3, 5708])

Outputs of the model:
- conv2d_out: torch.Size([1, 8, 64, 64])