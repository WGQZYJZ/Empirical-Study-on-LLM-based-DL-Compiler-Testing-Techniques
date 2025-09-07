
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(32, 8, 4)
        self.bn   = torch.nn.BatchNorm2d(8)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):

        v1  = self.conv(x1)
 
        # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v2 = (v1 > 0).type_as(v1)
 
        # Multiply the output of the transposed convolution by the negative slope.
        v3 = v1 * negative_slope

        # Apply the where function to select elements from v1 or v3 based on the mask v2
        v4 = torch.where(v2, v1, v3).view(-1)  # Selects elements in the output of the convolution or multiplies by the negative slope if there are zeros present

        return self.relu


# Initializing the model
m  = Model()
