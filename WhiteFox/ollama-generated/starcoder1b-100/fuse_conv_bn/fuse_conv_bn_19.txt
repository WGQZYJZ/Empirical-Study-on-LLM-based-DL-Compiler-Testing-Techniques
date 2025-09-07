
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, y1):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = torch.cat((y1, x1), dim=1)
        return self.conv_bn(v1, 3)(v2)

    def conv_bn(self, x1, X):
        # X can be either 1 or 2 representing the dimension
        if X in [1, 2]:
            return torch.nn.functional.conv2d(x1, torch.randn((1, 4, 6, X))), \
                   torch.nn.BatchNorm2d(X)

        elif X in [3]:
            return torch.nn.functional.conv3d(x1, torch.randn((1, 5, 7, 8, 9))), \
                   torch.nn.BatchNorm3d(9)

        else:
            raise NotImplementedError


# Inputs to the model
input_tensor = torch.randn(2, 4, 6, 2)
output = Model()(input_tensor, input_tensor, input_tensor)


