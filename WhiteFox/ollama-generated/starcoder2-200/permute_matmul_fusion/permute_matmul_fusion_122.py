
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(2)
        v2  = input_tensor_A.permute(0).unsqueeze(-1) # or input_tensor_B.permute(0), etc.
        v3  = torch.bmm(v1, v2)  # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = input_tensor_A.expand(-1, -1, 4).permute(0, 2, 1) # or input_tensor_B.expand(-1, -1, 4), etc. 
__output__  = m(x1)

