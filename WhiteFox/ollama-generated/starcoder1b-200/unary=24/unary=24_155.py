
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.relu  = torch.nn.LeakyReLU(negative_slope=negative_slope)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1 * negative_slope, v1) # Apply the where function to select elements from t1 or t3 based on the mask t2
        v3 = self.relu(v2)  # Apply the Leaky ReLU activation function
        return v3


# Initializing the model
m = Model()

