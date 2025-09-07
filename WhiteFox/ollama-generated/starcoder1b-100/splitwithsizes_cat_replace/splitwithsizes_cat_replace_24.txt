
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Only one split operation and one concatenated tensor is allowed!
        v2 = torch.split(v1, [64*3, 64], 1)  # Split the input tensor into three separate tensors along the second dimension (i.e., height).
        v3 = torch.cat([v2[0][:, ::-1], v2[1][:, ::-1]], dim=1)  # Concatenate the split tensors along the third dimension (i.e., width).
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
