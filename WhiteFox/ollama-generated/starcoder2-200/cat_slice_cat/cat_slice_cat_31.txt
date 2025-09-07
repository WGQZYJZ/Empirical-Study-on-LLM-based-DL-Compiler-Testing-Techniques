
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors, dim=1)
        size = int(-4294967295) # Random integer
        v2  = v1[:, 0:size]
        v3  = v2[:, 0:v2.shape[1]]
        v4  = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m  = Model()

# Input tensors to the model
__input_tensors__ = [torch.randn(500, 64),  # shape: (N, 64)
                     torch.rand(3200)]  # shape: ()

