
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 32, kernel_size=3, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 > 0).float() * -0.5
        v3 = (v1 > 0).float() * 2 + 0.7071067811865476 # Multiply the output of the transposed convolution by 2 or 0.7071067811865476, respectively
        v4 = torch.where(v2, x1, v3) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v4


# Initializing the model
m = Model()

