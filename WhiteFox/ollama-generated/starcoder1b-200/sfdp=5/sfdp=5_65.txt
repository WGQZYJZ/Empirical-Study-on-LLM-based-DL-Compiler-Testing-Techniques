
class Model(torch.nn.Module):
    def __init__(self, hidden_size=32):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(hidden_size * 4, 3)

    def forward(self, x):
        # Compute the output shape
        nbatch, ncrops, c, h, w = x.shape

        # Generate input features from each crop
        x1 = torch.zeros((nbatch, 8 * h, w))
        for i in range(ncrops):
            x1[:, i * h: (i + 1) * h, :] = self.conv1(x[i])

        x2 = torch.zeros((nbatch, 16 * h, w))
        for i in range(ncrops):
            x2[:, i * h: (i + 1) * h, :] = self.conv2(x[i])

        # Concatenate input features to form input feature matrix
        x = torch.cat((x1, x2), dim=1)

        # Compute the output
        x = self.fc(torch.tanh(self.fc(x)))

        return x


# Initializing the model
m = Model()


