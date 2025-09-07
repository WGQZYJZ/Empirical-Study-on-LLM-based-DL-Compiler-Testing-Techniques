
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dtype = torch.float32
        self.layout = 'cuda'
        self.device = torch.device('cuda')
 
    def forward(self, x1, y2, z3):
        v1  = torch.full([x1, y2], 1., dtype=self.dtype, layout=self.layout, device=self.device, pin_memory=False)
        v2 = convert_element_type(v1, self.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Inputs to the model
x1  = torch.randn(3, 64, 64)
y2  = torch.randn(3, 64, 64)
z3  = torch.randn(64, 64, 3)
__output__  = Model()(x1, y2, z3)

