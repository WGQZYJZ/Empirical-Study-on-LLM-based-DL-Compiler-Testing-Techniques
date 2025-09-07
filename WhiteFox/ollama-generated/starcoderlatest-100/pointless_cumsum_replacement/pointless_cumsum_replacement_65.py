
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([3, 64, 64], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self):
        v2 = convert_element_type(self.t1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
