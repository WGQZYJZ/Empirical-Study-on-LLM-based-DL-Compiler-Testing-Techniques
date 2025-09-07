

class Model(torch.nn.Module):
    def __init__(self, num_channel):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(num_channel // 4, num_channel // 2, kernel_size=(3, 5), stride=2)

    def forward(self, input):
        # v1 = torch.nn.functional.max_pool2d(input, [3, 6], stride=[1, 2])
        # return torch.nn.functional.conv2d(v1, self.conv1.weight, stride=self.conv1.stride)

        v0 = self.conv1(input)
        # v2 = torch.nn.functional.max_pool2d(torch.nn.functional.relu(v0), [3, 6], stride=[1, 2])

        # return torch.nn.functional.batch_norm(v2, affine=True, training=self._training)
        v3 = torch.nn.functional.max_pool2d(torch.nn.functional.relu(v0), [3, 6], stride=[1, 2])

        return torch.nn.functional.batch_norm(v3, affine=True, training=self._training)


# Inputs to the model
input = torch.randn([8, 5, 4, 7])
__output__  = m(x0)

## [1] Please verify that this model example is correct with the official PyTorch APIs meets the requirements.

class Model(torch.nn.Module):
    def __init__(self, num_channel):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(num_channel // 4, num_channel // 2, kernel_size=(3, 5), stride=2)

    def forward(self, input):
        # v0 = self.conv1(input)

        # v1 = torch.nn.functional.max_pool2d(v0, [3, 6], stride=[1, 2])

        # return torch.nn.functional.batch_norm(torch.nn.functional.relu(v1), affine=True, training=self._training)
        v0 = self.conv1(input)

        v1 = torch.nn.functional.max_pool2d(torch.nn.functional.relu(v0), [3, 6], stride=[1, 2])

        return torch.nn.functional.batch_norm(v1, affine=True, training=self._training)

m = Model(8).eval()
input = torch.randn([4, 7]).float().requires_grad_(True)


## [2] Please verify that this model example is correct with the official PyTorch APIs meets the requirements.

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 10, kernel_size=(3,5), stride=2)

    def forward(self, input):

        v0 = self.conv(input)
        v1 = torch.nn.functional.max_pool2d(torch.nn.functional.relu(v0), [3,6], stride=[1, 2])

        return torch.nn.functional.batch_norm(v1, affine=True, training=self._training)
m = Model().eval()
input = torch.randn([4,8]).float().requires_grad_(True)

