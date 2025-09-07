
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1=0, arg2=1):
        v1 = torch.full([arg1, arg2], 1)
        v2 = convert_element_type(v1, dtype='float32')
        v3 = torch.cumsum(v2, 1)
