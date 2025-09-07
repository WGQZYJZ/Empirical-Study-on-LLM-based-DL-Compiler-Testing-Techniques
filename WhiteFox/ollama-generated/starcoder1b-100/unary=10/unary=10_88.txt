
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
        self.linear1 = torch.nn.Linear(16 * 4 * 4, 120)
        self.linear2 = torch.nn.Linear(120, 84)
        self.linear3 = torch.nn.Linear(84, 10)
 
    def forward(self, x):
        v = torch.nn.functional.leaky_relu(
            self.conv1(x), inplace=True
        )
        v = torch.nn.functional.batch_norm(v, 0, True, False, True, 0.001)
        v = torch.nn.functional.leaky_relu(
            self.conv2(v), inplace=True
        )
        v = torch.reshape(v, (v.shape[0], -1))
        v = torch.nn.functional.leaky_relu(
            self.linear1(v), inplace=True
        )
        v = torch.nn.functional.dropout(
            v, p=0.1, training=self.training)
        v = torch.nn.functional.leaky_relu(
            self.linear2(v), inplace=True
        )
        v = torch.nn.functional.dropout(
            v, p=0.1, training=self.training)
        v = self.linear3(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
