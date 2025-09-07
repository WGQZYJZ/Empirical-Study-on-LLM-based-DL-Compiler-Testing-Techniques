
class Model(torch.nn.Module):
    def __init__(self, size=50):
        super().__init__()
 
    def forward(self, input1):
        v1 = torch.cat(input1) 
        v2 = v1[:, 0:9223372036854775807] # This is a random slice
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1) 
        return v4


# Initializing the model