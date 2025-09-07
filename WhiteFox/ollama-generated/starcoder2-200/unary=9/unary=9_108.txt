
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v4  = v2 / 6
        
        # NOTE: the output of this operation is clamped to a minimum of 0 and maximum of 5;
        #       it should be modified accordingly in order for the result to meet the requirements.
        v3  = torch.clamp_min(v4, 1)

        return v3


# Initializing the model
m = Model()


# Inputs to the model