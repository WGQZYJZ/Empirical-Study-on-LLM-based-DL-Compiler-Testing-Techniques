
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type_as(v1) # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise. The type_as function converts the type of v1 to match the type of this operation.
        v3  = negative_slope * (torch.abs(v2 - 1) + torch.abs(- v2)) # Multiply each element of the boolean mask by the negative slope. The type_as function converts the type of this multiplication to match the type of v1. 
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing and running the model