
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.cat([x2, x3], dim=1)
        v4  = torch.cat([v0[0:9223372036854775807][0:size + 2]], dim=1)
        return v4


# Initializing the model
m  = Model()
 
__input_tensors__ = [torch.randn(1, 3, 64, 64), torch.randn(1, size+2, 70, 58)] 
 
__output__  = m(*__input_tensors__)
