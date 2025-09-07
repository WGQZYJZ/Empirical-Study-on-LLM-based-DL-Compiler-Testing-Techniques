
class Model(torch.nn.Module):
    def __init__(self, num_layers):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
        self.relu = torch.nn.ReLU()

        self.conv = [torch.nn.Conv2d(i, i * 2, 3) for i in range(num_layers)]
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=1)

    def forward(self, x):
        v1 = x.view(x.shape[0], -1)

        for idx in range(len(self.conv)):
            conv_layer = self.conv[idx]
            v2 = conv_layer(v1)

            pool_layer = self.pool if idx == num_layers - 1 else torch.nn.AvgPool2d(kernel_size=2, stride=1)
            v3 = pool_layer(v2)

            v1 = torch.cat([v1, v2], dim=-1)

        v1 = self.relu(self.linear(v1))
        return v1


# Initializing the model
m = Model(num_layers=2)


