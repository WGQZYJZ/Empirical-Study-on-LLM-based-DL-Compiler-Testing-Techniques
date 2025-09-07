
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)
        v3 = t1[:, 0:size]
        return v3


# Initializing the model
m = Model()
# Inputs to the model
input_tensors = (torch.randn(1, 3, 64, 64), torch.randn(1, 3, 64, 64))
