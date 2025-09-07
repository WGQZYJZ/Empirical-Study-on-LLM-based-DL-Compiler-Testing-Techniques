
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)

    def forward(self, x1):
        l1 = self.conv(x1) # Apply linear transformation to the input tensor

        clamped = torch.clamp(l1 + 3, min=0) # Clamp the output of the linear transformation added with 3 between 0 and 6
        scaled_out = clamped / 6  # Divide the clamped output by 6
        return scaled_out

# Initializing the model
m = Model()

