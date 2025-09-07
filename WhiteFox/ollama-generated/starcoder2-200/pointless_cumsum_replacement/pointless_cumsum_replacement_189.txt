
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, arg1=32768L, arg2=500L):  # Using different parameters on the arguments
        v1 = torch.full([arg1, arg2], 1, dtype=torch.float32)
        v2 = convert_element_type(v1, torch.float32) 
        v3 = torch.cumsum(v2, 1)

        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4096, 500L)

