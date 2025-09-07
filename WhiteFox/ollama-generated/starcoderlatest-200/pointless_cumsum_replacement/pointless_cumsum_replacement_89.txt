
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([3, 6], 1, dtype=torch.float, layout=torch.row_major, device=x1.device)
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
