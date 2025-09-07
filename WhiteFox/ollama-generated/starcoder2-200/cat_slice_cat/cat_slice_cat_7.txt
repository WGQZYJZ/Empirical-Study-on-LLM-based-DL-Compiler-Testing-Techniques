
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size=9223372036854775807):  # pylint: disable = arguments-differ
        v1  = torch.cat([x1], dim=1)
        v2  = v1[:, :size] 
        return v2


# Initializing the model with custom argument size
m  = Model(size=1430958655) 

