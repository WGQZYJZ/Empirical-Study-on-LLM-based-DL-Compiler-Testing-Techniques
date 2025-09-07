
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=16, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        # Apply the where function to select elements from t1 or t3 based on the mask t2. 
        v4 = torch.where(v1 > 0, v1, -5)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
