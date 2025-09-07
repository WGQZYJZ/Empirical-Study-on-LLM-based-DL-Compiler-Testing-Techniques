
class ResNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7) # Apply transposed convolution with kernel size 7 to the input tensor
        self.relu1 = nn.ReLU() # Apply ReLU nonlinearity to the output of transposed convolution
        self.pool1 = nn.MaxPool2d(kernel_size=3, stride=2) # Apply max-pooling with a stride of 2 to the output of transposed convolution
        self.conv2 = nn.Conv2d(64, 192, kernel_size=7) # Apply transposed convolution with kernel size 7 to the output of max-pooling
        self.relu2 = nn.ReLU() # Apply ReLU nonlinearity to the output of transposed convolution
        self.pool2 = nn.MaxPool2d(kernel_size=3, stride=2) # Apply max-pooling with a stride of 2 to the output of transposed convolution
        self.conv3 = nn.Conv2d(192, 384, kernel_size=7) # Apply transposed convolution with kernel size 7 to the output of max-pooling
        self.relu3 = nn.ReLU() # Apply ReLU nonlinearity to the output of transposed convolution
        self.conv4 = nn.Conv2d(384, 256, kernel_size=7) # Apply transposed convolution with kernel size 7 to the output of max-pooling
        self.relu4 = nn.ReLU() # Apply ReLU nonlinearity to the output of transposed convolution
        self.conv5 = nn.Conv2d(256, 128, kernel_size=3) # Apply a pointwise convolution with kernel size 7 to the input tensor
        self.fc = nn.Linear(41792, 10)
 
    def forward(self, x1):
        v1 = F.adaptive_avg_pool2d(x1, 1) # Get the output of max-pooling
        v1 = self.relu1(v1) # Apply ReLU nonlinearity to the output of the max-pooling
        v2 = self.pool1(self.conv1(v1)) # Apply transposed convolution with kernel size 7 to the output of max-pooling
        v3 = F.adaptive_avg_pool2d(x1, 1) # Get the output of max-pooling
        v3 = self.relu2(v3) # Apply ReLU nonlinearity to the output of the max-pooling
        v4 = self.pool2(self.conv2(v3)) # Apply transposed convolution with kernel size 7 to the output of max-pooling
        v5 = F.adaptive_avg_pool2d(x1, 1) # Get the output of max-pooling
        v5 = self.relu3(v5) # Apply ReLU nonlinearity to the output of the max-pooling
        v6 = self.pool2(self.conv3(v5)) # Apply transposed convolution with kernel size 7 to the output of max-pooling
        v7 = F.adaptive_avg_pool2d(x1, 1) # Get the output of max-pooling
        v7 = self.relu4(v7) # Apply ReLU nonlinearity to the output of the max-pooling
        v8 = self.pool2(self.conv4(v7)) # Apply transposed convolution with kernel size 3 to the output of max-pooling
        v9 = F.adaptive_avg_pool2d(x1, 1) # Get the output of max-pooling
        v9 = self.relu5(v9) # Apply ReLU nonlinearity to the output of the max-pooling
        v10 = self.conv5(v9) # Apply a pointwise convolution with kernel size 3 to the input tensor
        v10 = torch.flatten(v10, 1) # Flatten all dimensions of the input tensor, so that it only stores the channel dimension of the flattened output
        v10 = self.fc(v10) # Apply a linear classifier to the flattened output
        return F.log_softmax(v10, dim=-1)


# Initializing the model
m = ResNet()

