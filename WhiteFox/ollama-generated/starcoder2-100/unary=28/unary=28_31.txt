
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v3 = torch.clamp_max(x1 + 5, max=20) # Adding 5 to the output of the previous operation and clamping the output of the operation to a maximum value of 20
        return v3


# Initializing the model