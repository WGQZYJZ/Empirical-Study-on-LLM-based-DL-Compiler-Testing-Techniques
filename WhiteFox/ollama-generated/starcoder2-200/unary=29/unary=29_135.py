
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):

        v2  = torch.clamp_min(input1, -50)
        return v2

# Initializing the model