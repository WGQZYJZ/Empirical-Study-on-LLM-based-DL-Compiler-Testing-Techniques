
class Model(torch.nn.Module):
    def __init__(self, dtype=torch.float32, layout=torch.strided, device="cpu"):
        super().__init__()
        self.t1 = torch.full([3, 64, 64], 1.0, dtype=dtype, layout=layout, device=device, pin_memory=False)

    def forward(self):
        t2 = convert_element_type(self.t1, dtype)
        t3 = torch.cumsum(t2, dim=1)
        return t3


# Initializing the model and computing output
m = Model()
out = m()

