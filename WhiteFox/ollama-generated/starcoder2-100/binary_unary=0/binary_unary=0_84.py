
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor # Adding another tensor to the convolution output 
        return torch.relu(v2), other_tensor # ReLU activation function is applied to the result


# Initializing the model
m = Model()

