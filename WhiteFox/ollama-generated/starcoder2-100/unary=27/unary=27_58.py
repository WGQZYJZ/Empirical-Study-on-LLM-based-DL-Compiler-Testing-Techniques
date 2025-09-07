
class Model(torch.nn.Module):
    def __init__(self, min_value=-20, max_value=15):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=args.min_value) # Apply a clamping operation to the convolution output with the minimum value provided as a keyword argument 
        v3  = torch.clamp_max(v2, max_value=args.max_value)# Apply another clamping operation to the previous convolution output with the maximum value provided as a keyword argument
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model