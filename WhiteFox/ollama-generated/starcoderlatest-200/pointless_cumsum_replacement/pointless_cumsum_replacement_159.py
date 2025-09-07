
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.size(0), x2.size(1)], 1, dtype=torch.float32, device='cuda', layout=torch.strided) # Create a tensor filled with the scalar value 1, with the specified dtype and device
        v2 = convert_element_type(v1, torch.int64)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).cuda()
x2 = torch.randn(1, 8, 32, 32).cuda()
