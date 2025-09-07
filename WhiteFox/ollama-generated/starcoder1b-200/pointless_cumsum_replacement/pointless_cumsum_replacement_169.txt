
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x1):
        v1 = self.t1 * 0.5
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()


