
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0  # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = torch.where(mask, v1, self.negative_slope * x1)  # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v2


# Initializing the model
m = Model()


