
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3,8, 1,stride=1)
        self.conv2 = torch.nn.Conv2d(8,8, 1,stride=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1) 
        v2 = v1 + other # Adding another tensor to the output of the convolution1
        v3 = F.relu(v2)# Applying the ReLU function on the result
        return v3


# Initializing the model