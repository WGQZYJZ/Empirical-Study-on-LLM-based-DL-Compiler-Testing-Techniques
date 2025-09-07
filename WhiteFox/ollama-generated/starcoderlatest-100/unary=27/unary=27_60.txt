
class Model(torch.nn.Module):
    def __init__(self, min_value: int = 0, max_value: int = 255):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with different minimum and maximum values
m1 = Model(0.5, 254)
x1 = torch.randn(1, 3, 64, 64)
__output1__ = m1(x1)


# Description of requirements
You are going to create a model that generates inputs with values in [50, 255]. Use the code snippet below as a template. Please change the function `model` to generate a model that is different from the previously one, and you are welcome to add additional layers (e.g., BatchNorm or Conv+BatchNorm) to the model if needed.


# Model
class Model(torch.nn.Module):
    def __init__(self, min_value: int = 50, max_value: int = 255):
        super().__init__()
        # Add additional layers (e.g., BatchNorm or Conv+BatchNorm) to the model if needed
 
    def forward(self, x1):
        v1 = torch.clamp_min(x1, min_value)  # Clamp all values in the input tensor to a minimum value
        v2 = torch.clamp_max(v1, max_value)  # Clamp all values in the previous operation to a maximum value
        return v2


# Initializing the model with different minimum and maximum values
m1 = Model()
x1 = torch.randn(1, 3, 64, 64)
__output1__ = m1(x1)
