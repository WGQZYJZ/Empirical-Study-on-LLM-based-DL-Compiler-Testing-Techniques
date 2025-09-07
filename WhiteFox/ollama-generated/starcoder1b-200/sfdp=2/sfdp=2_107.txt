
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)
 
    def forward(self, x1):
        # Step 1: Pointwise convolution with kernel size 1 to the input tensor
        v1 = self.conv1(x1)  # shape is torch.Size([B, 8, H/S, W/S])
        v2 = v1 * 0.5  # multiply v1 by 0.5 and store result in v2
        # Step 2: Multiply the output of the convolution by 0.7071067811865476
        v3 = v1  # store the input tensor as a copy so that it does not influence the next line
        v3 *= 0.7071067811865476  # multiply v2 by 0.7071067811865476
        # Step 3: Apply error function to the output of the convolution
        v4 = torch.erf(v3)  # compute the error function of v3 and store it in v4
        # Step 4: Add one to the result of the error function
        v5 = v4 + 1  # add 1 to v4 and store it in v5
        # Step 5: Multiply the result of the convolution by the output of the error function
        v6 = v2 * v5  # multiply v2 by v5, store it in v6
        return v6


# Initializing the model
m = Model()


