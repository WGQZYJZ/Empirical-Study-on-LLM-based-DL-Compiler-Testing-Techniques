
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).type(torch.cuda.FloatTensor) * negative_slope  # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        return torch.where(mask, x1, 0.5*x1 - mask + 2*v1)  # Apply the where function to select elements from t1 or t3 based on the mask t2


# Initializing the model
m = Model()


