
class Model(torch.nn.Module):
    def __init__(self, size=9223372036854775807):
        super().__init__()
 
    def forward(self, *tensors):
        v1  = torch.cat([tensors[i] for i in range(len(tensors))], dim=1)
        v2  = v1[:, :9223372036854775807]
        v3  = v2[:, size:]
        v4  = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model