
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x1):
        return self.t1 + 1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn([arg1, arg2], dtype=dtype, layout=layout, device=device, pin_memory=False)
