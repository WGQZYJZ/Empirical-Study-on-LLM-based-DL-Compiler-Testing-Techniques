
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        conv = torch.nn.Conv2d(3, 8, kernel_size=5)
        
        bn = torch.nn.BatchNorm2d(8)
        
        output = bn(conv(x1))
        
        return output


# Initializing the model