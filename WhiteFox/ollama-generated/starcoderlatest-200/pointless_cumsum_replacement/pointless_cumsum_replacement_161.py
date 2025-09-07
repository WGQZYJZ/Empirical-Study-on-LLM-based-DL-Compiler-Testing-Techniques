
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor, out_dtype=torch.float32, layout=torch.strided):
        v1 = torch.full([input_tensor.size()[0], 1], 1.0, dtype=out_dtype, device='cuda', layout=layout) 
        v2 = convert_element_type(v1, input_tensor.dtype)
        v3 = torch.cumsum(v2, dim=1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 64, 64).cuda() # (4, 8, 64, 64) on GPU0
