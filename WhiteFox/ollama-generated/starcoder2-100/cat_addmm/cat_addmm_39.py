
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v0 = torch.addmm(input1, input2) # Matrix multiplication
        v1  = v0 + 1   # Addition
        v3 = self.__dim_concat__(v0, 3)
        return v1, v3

    def __dim_concat__(self, input, dim):
        result = torch.cat([input], dim=dim)

# Initializing the model
m = Model()

# Inputs to the model
input1  = torch.randn(4096, 512) # The first matrix in the 3D tensor. Size: [4096 x 512]
input2  = torch.randn(4096, 80)  # The second matrix in the 3D tensor. Size: [4096 x 80]

