
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1) 
        mask = (v1 > 0).type(torch.FloatTensor)
        v2 = torch.nn.functional.relu6(v1 * -mask + v1 * mask)
        return v2


# Initializing the model and setting negative slope to 0.5
m = Model()
