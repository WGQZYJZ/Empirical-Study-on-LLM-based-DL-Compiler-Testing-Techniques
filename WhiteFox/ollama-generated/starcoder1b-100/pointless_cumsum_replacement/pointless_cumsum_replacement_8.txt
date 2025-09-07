
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v3 = convert_element_type(t2, dtype)
        v4 = t2 + 1
        v5 = v1 * v4
        v6 = v5  + 1
        return v6


# Initializing the model
m = Model()


