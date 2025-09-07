
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x_sizes = torch.tensor([3], device='cuda')
        return self.conv(torch.split(x1, x_sizes, dim=-1))


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
__output__  = m(input_tensor)


