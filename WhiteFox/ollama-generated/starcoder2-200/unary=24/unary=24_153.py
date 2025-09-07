
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0 # create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise

        v2 = torch.where(mask, v1, -v1*self.negative_slope) # apply the where function to select elements from t1 or t3 based on the mask
        return v2

# Initializing the model
model  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
model (x1)