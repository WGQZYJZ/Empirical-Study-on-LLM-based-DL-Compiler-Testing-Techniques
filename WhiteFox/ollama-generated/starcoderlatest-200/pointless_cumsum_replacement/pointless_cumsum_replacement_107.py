
class Model(torch.nn.Module):
    def __init__(self, input_shape=(3, 64, 64), channel=8, kernel_size=1, stride=1, padding=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_shape[0], channel, kernel_size, stride, padding)
 
    def forward(self, x1, dtype=None, layout=torch.strided, device=None, pin_memory=False):
        t1 = torch.full([x1.shape[0]], 1, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
dtype = x1.dtype
layout = x1.layout
device = x1.device
pin_memory = True
