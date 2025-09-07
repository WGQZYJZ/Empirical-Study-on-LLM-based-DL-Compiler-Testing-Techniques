
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.linear1 = torch.nn.Linear(256, 10)

    def forward(self, x1):
        w = F.leaky_relu(self.conv1(x1), negative_slope=0.3, inplace=True)
        a = self.linear1(w).contiguous()  # Compute linear projection
        a = F.dropout(a, training=self.training, p=dropout_p)  # Apply dropout on the linear projections
        w = F.leaky_relu(self.conv2(w), negative_slope=0.3, inplace=True)
        b = self.linear1(w).contiguous()  # Compute linear projection
        b = F.dropout(b, training=self.training, p=dropout_p)  # Apply dropout on the linear projections
        return a + b


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
