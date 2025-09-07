

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d_layer1 = torch.nn.Conv1d(in_channels, out_channels, kernel_size, stride=stride, padding=padding)
        self.conv1d_layer2 = torch.nn.Conv1d(in_channels, out_channels, kernel_size, stride=stride, padding=padding)
 
    def forward(self, x):
        x = x.contiguous().view(-1, in_channels) # Make sure the dimension of the input is reduced to a vector
        h1 = self.conv1d_layer1(x)
        h2 = self.conv1d_layer2(x)
 
        return h1 + h2


# Inputs to the model
x  = torch.randn(8, 4000)
