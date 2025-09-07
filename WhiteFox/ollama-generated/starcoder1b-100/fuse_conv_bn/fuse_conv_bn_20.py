
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # Input X should match with X
        self.bn  = torch.nn.BatchNorm2d(...)
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.conv2d(v1, self.conv.weight, self.conv.bias) # Fuse the convolution layer with batch normalization
        v3 = torch.nn.functional.batch_norm(v2, training=self.training) # Remove the batch normalization layer from graph
        v4 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        return v4


# Initializing the model
m = Model()
