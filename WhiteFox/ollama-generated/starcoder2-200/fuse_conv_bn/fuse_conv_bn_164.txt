
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.conv3d(x1)  # Apply conv 3d on input tensor
        v2 = v * torch.nn.functional.batch_norm(v, None, True, True, eps=0.)  
        return v

# Initializing the model
m  = Model()

 # Inputs to the model: Input tensor shape (16, 4, 5)
#                       3d input: Input tensor shape (16, 3, 2, 5) 
x1 = torch.randn(10, 4, 5).permute([0, 2, 1])

__output__  = m(x1)

