
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        v2 = v1 * negative_slope
        out = torch.where(mask, v2, v1)  # Apply the where function to select elements from t1 or t3 based on the mask t2
        return out


# Initializing the model
m = Model()
negative_slope = 0.5
