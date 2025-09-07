
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.full([100], 1, dtype=x1.dtype, device=x1.device)
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Input tensors to the model:
x1  = torch.randn(5, 3, 64, 64)
x2  = torch.randn(8, 3, 64, 64)

