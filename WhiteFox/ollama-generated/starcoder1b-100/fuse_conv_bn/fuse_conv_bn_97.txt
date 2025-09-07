
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNorm2d(...)
        self.relu  = torch.nn.ReLU()
        self.maxpool  = torch.nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))
        self.linear  = torch.nn.Linear(in_features=4 * 4 * 2 * 100, out_features=6)

    def forward(self, x):
        # The first 4 times of each filter are fused into a single convolution layer
        x = self.relu(self.conv(x))

        # Batch normalization is applied on the convolution output and added to the graph
        bn = torch.nn.functional.batch_norm(input=x, gamma=torch.ones((100,)), running_mean=torch.zeros((100,)), eps=1e-5)  # X should match with ConvXd

        # The batch normalization is removed from the graph
        bn = self.maxpool(bn)

        # Finally, a linear layer is added to the graph and fused with the output of the first convolution layer. 
        x = self.relu(self.linear(x))

        return x


# Initializing the model
m = Model()
m.eval()


