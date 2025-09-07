
class FusedModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v3  = torch.nn.functional.batchnorm(x1, momentum=0.9) # Use the functional API to fuse batch norm
         return v3


m = FusedModel()
__output__  = m(x1)


