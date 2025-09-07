
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.split(x1, 256)
        v1 = [v[i] for i in range(len(v)) if i in [0]]
        return concat_tensors(v1)


# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(256, 384, 9) # This input is not valid for the model since it does not match the shape required by the split operation

