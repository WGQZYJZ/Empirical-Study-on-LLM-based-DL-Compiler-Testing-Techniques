
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8 * 64 * 64, 1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.where(v1 > 0., v1, -v1)
        # return the output of the linear transformation from the convolution
	v3 = v2 * (-0.7071) # this is equivalent to the following:
        # v3 = 1 / (abs(1.) + abs(-0.7071))
        v3 = 1 - torch.log(-torch.exp(1. / (abs(v1) + abs(-0.7071))))
	return self.linear(v3)


# Initializing the model
m = Model()

