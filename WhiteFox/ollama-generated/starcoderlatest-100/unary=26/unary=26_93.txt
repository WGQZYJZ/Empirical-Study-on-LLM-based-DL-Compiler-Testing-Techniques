
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        negative_slope = -torch.tensor([[[[0.]]]], dtype=torch.float32)
        v3 = v1 * negative_slope 
        v4 = torch.where(v2 > 0, v1, v3).clamp(-1., 1.) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
