
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Create a boolean mask where each element is True if the corresponding element in v1 is greater than or equal to 0.25 and smaller than or equal to 0.75, False otherwise
        b1 = (v1 >= 0.25) & (v1 <= 0.75)
        v2 = torch.where(b1, v1 * 0.39215686274509803, v1) # Apply the where function to select elements from v1 or v2 based on mask b1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
