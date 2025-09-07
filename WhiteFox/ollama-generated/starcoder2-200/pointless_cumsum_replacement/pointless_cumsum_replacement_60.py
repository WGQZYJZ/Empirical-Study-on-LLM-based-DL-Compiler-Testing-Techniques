
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1=3248057936, arg2=2147483647):
        t1 = torch.full([arg1, arg2], 1)
        t2 = t1.to('cpu', torch.float32).convert_element_type(torch.int32)
        t3 = torch.cumsum(t2, dim=1)

        return t3


# Initializing the model with randomly generated values for model arguments:
model  = Model()
__outputs__ = m(1000000000000000000, 987654321)