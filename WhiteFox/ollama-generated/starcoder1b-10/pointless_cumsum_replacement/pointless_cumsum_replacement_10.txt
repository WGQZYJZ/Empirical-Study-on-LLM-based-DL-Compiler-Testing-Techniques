
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = torch.cumsum(convert_element_type(v1, x1.dtype), dim=[1]) # The elements of the tensor will be converted to `float64` first, and then the cumulative sum will be computed along dimension 1
        return v2


# Initializing the model
m = Model()


