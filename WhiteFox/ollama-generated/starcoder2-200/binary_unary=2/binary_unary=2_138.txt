
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = torch.randn((1), requires_grad=True)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other # "other" is the output of a pointwise convolution with kernel size 1 applied to another image, and there are two other tensors or scalars that you need to construct the model
        v3  = torch.nn.functional.relu(v2)
        return v3


# Initializing the model