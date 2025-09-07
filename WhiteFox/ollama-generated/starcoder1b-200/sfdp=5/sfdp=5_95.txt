
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.fc = torch.nn.Linear(4096, 1)
 
    def forward(self, x):
        v1 = F.relu(self.conv1(x))
        v2 = F.relu(self.conv2(v1))
        return self.fc(torch.flatten(v2, 1))


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
y = m(x)

# Expected outputs for different values of dropout_p
expected_output0 = y[7, 2]
expected_output1 = (1 - 0.5 * y[7, 2]) * y[7, 2] + 0.7071067811865476 * y[14, 9]
assert np.allclose(expected_output0, expected_output1)

