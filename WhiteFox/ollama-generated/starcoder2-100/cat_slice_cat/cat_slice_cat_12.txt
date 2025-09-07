
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1):
        v1 = torch.cat([t1, t1], dim=2)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, :, :size]
        return torch.cat([v1, v3], dim=2)

# Initializing the model with the input size specified in the model
m  = Model()
size  = 96

# Inputs to the model
t1  = torch.randn(10804757, size, 96039)

