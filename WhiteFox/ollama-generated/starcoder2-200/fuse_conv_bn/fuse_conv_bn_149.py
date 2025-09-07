
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.conv2d(x1, self.conv1())

        conv3  = torch.nn.ConvNd(2, 4)
        conv3_out = torch.nn.functional.conv2d(v1, conv3())
        bn3_out  = torch.nn.functional.batch_norm(conv3_out)
        return bn3_out

    def conv1(self):
        return torch.nn.ConvNd(4, 5, stride=4, padding=0)

# Initializing the model and inputs to the model
m = Model()
x1 = torch.randn(1, 2, 3)
m(x1)

