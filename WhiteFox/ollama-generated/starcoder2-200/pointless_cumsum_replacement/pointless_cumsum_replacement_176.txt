
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device) # [arg1, arg2]
        v2 = convert_element_type(v1, dtype)
        return torch.cumsum(v2, 0).cuda()

# Initializing the model
m = Model().cuda(device)

