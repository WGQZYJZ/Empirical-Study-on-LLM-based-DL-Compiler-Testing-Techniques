
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        output1 = self.conv(x1)
        if len(output1) != 1:
            raise ValueError('Number of outputs must be 1 but {} found.'.format(len(output1)))
        output2 = self.conv(output1[0])
        return output2


# Initializing the model
m = Model()


