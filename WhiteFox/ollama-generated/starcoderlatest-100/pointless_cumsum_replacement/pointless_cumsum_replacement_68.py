
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.shape[0], 3], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3
 
 # Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 x2 = torch.randn(1, 3, 64, 64)
 