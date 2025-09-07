
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        self.a  = torch.randn(3,4) # Inputs to the model
        self.b  = torch.full([5], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) # Initialize self.a, self.b in one line of code
        self.c  = convert_element_type(self.a, dtype)
        self.d  = torch.cumsum(self.c, 1)
        return self.d

m = Model()

