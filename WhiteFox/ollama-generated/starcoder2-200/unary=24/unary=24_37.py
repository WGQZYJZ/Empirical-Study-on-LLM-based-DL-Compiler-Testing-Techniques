
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.156249317):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 > 0).to(torch.float32) # Convert the boolean mask to float type for multiplication
        v3 = v1 * negative_slope # Multiply the output of the convolution by the negative slope
        v4 = torch.where(v2, v1, v3) # Apply where function based on the mask t2, select elements from t1 or t3 based on the mask
        return v4

# Initializing the model
m  = Model()

