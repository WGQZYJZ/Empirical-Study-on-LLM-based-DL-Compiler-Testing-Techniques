
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 8192)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, -1)) # Flatten the input tensor and perform a linear transformation with a size of (number of pixels in one image times number of channels in one image times width of one image times height of one image) x 8192 to flattened output
        v2 = v1 - other_input  # Subtract 'other_input' from the output of the linear transformation with the previous input tensor
        v3 = torch.nn.functional.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
