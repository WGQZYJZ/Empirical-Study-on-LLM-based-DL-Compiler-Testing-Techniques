
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dtype = torch.float32
        self.layout  = 'NCHW'
        self.device  = torch.device('cuda:0')
        self.pin_memory = True

    def forward(self, x1):
        t1 = torch.full([arg1, arg2], 1, dtype=self.dtype, layout=self.layout, device=self.device, pin_memory=self.pin_memory)
        return convert_element_type(t1, self.dtype),


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 64, 64)
__output__ , __grad__ = m.forward(x1)


