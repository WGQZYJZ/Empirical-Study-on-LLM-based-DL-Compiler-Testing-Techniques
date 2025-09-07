
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, other=0.7071067811865476):
        v1  = self.conv(x1) # Apply a pointwise convolution to the input tensor
        v2  = torch.nn.Linear()(v1) - 0.5 
        return v2

m  = Model()
x1  = torch.randn(1, 3, 64, 64)

