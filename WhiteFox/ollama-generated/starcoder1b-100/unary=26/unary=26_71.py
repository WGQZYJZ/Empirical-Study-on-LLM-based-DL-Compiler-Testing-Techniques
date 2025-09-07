
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0
        v2 = v1 * -2
        v3 = torch.where(v1, v1, v2)  # Apply the where function to select elements from v1 or v2 based on the mask v1
        return v3


# Initializing the model
m = Model()


