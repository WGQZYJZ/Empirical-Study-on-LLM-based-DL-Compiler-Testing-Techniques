
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        return convert_element_type(t1, dtype), torch.cumsum(convert_element_type(t1, dtype), 1)


# Initializing the model
m = Model()
 
__output__1__, __output__2__ = m(arg1, arg2)
 
