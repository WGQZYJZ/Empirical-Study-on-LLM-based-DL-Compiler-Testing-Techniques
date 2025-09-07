
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.fc = torch.nn.Linear(16 * 4 * 4, 10)
 
    def forward(self, x):
        # Apply the convolutional layers
        x = F.leaky_relu(F.max_pool2d(self.conv1(x), 2))
        x = F.leaky_relu(F.max_pool2d(self.conv2(x), 2))
 
        # Flatten the image and reshape it to a vector
        x = x.view(-1, self.get_num_channels(x))

        # Apply linear layers and apply activation functions
        x = self.fc(x)
        x = torch.nn.functional.softmax(x, dim=-1)
 
        # Apply pointwise convolutions
        x = F.leaky_relu(self.conv1(x))
        x = F.leaky_relu(self.conv2(x))

        return x


# Initializing the model
m = Model()

