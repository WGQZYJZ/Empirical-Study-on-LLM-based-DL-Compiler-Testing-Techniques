
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask_tensor = (v1 > 0).float()
        v3 = v1 * negative_slope
        v4 = torch.where(mask_tensor, v1, v3) # select elements from t1 or t3 based on the mask 
        return v4

# Initializing the model with a negative slope of `0.5`
m  = Model()


# Inputs to the model