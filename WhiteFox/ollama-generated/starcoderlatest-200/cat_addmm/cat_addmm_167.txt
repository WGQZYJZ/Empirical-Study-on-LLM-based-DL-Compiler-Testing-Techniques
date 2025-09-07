
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.conv = torch.nn.Conv1d(d_model, 8, 1)
 
    def forward(self, x1):
        v1 = torch.addmm(input, mat1, mat2) 
        t2 = torch.cat([v1], dim=1) # Concatenate the result along a specified dimension
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 512, 4096)
