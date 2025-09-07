
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, x2, x1) # TODO: Fill in the correct code here (Replace [ ] with your own code)
        v2 = torch.cat([v1], dim=0) # TODO: Concatenate two tensors along a dimension 0
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 64, 64) # TODO: Generate another tensor to use as mat2 here (Replace [ ] with your own code)
