
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8, bias=False)

    def forward(self, x1):
        l1  = self.conv(x1)
        l2  = l1 * (l1 + 3).clamp(0, 6) # Multiply the output of the linear transformation by clamped output of the linear transformation added with 3
        l3  = l2 / 8.  # Divide the output of multiplication by 8.0
        return l3


m = Model()

 x1  = torch.randn(1, 3)

__output__  = m(x1)

# Please check the output tensor is valid.