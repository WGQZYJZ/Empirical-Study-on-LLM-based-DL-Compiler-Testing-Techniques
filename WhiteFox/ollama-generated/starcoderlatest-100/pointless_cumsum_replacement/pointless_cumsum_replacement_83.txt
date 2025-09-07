
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.nn.FullNLLLoss()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], x2.shape[1]], 1, dtype=x2.dtype, layout=x2.layout, device=x2.device, pin_memory=False)
        v2 = convert_element_type(v1, x2.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 14, dtype=torch.float64)
x2 = torch.randn(1, 1, dtype=torch.int64)
