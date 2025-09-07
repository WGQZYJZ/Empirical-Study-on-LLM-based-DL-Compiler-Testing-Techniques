
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        # Do the following three things to obtain the desired output
        v1 = self.conv(x1) * 0.7071067811865476  # Use the linear transformation to multiply v1 by 0.7071067811865476
        v2 = torch.erf(v1)                  # Apply the error function
        v3 = t1 * negative_slope          # Multiply t1 by -0.5 * sqrt(pi)
        v4 = torch.where(t2, v1, v3)    # Choose v3 or v1 depending on whether t2 is True or not

        # And you are done!
        return v4


# Initializing the model
m  = Model()


