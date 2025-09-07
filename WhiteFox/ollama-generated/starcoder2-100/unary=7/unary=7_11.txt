

import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = torch.nn.Linear(25, 1024)
        self.fc2 = torch.nn.Linear(1024, 3)
        # the 3 layer
        self.conv_layer1 = torch.nn.Conv2d(in_channels=64, out_channels=196, kernel_size=(7, 7), stride=(1, 1))

        for param in self.conv_layer1.parameters():
            torch.nn.init.xavier_normal_(param)
            # Initialize the parameters of the conv layer using the Xavier normal method
        self.fc3 = torch.nn.Linear(256 * 7* 7, 4096)

        for param in self.fc1.parameters():
            torch.nn.init.xavier_normal_(param)
            # Initialize the parameters of the fully connected layer using Xavier normal method
        self.drop = torch.nn.Dropout(p=0.5, inplace=False)
        # Apply dropout with probability 0.5 and do not place it in-place

        for param in self.fc2.parameters():
            torch.nn.init.xavier_normal_(param)
            # Initialize the parameters of the fully connected layer using Xavier normal method

        self.softmax = torch.nn.Softmax(dim=0)

    def forward(self, X):
        # 6.4 Convolution layer, output size: (N, 196, H/4, W/4),
        # followed by Batch normalization and ReLU:
        conv_output = self.conv_layer1(X)

        conv_output = torch.nn.BatchNorm2d()(conv_output)
        # batch normalization layer: 6.5 ConvLayer (kernel size is 7*7, stride 1, padding 3), followed by Batch normalization and ReLU
        batch_norm_relu = torch.nn.ReLU(inplace=False)(conv_output)

        conv_output = self.drop(batch_norm_relu)
        # Add dropout to the layer with probability of dropping is 0.5

        # 6.8: Pooling layer, using 2*2 max pooling: (N, 196, H/4, W/4) -> (N, 196, H/4, W/4), and then add batch normalization on the pooled output
        pool_output = torch.nn.MaxPool2d(kernel_size=3, stride=(2,), padding=0)(batch_norm_relu)

        conv_output = self.conv_layer1(pool_output)

        conv_output = torch.nn.BatchNorm2d()(conv_output)
        # batch normalization layer: 6.5 ConvLayer (kernel size is 7*7, stride 1, padding 3), followed by Batch normalization and ReLU
        pool_output = self.softmax(self.fc1(pool_output))

        conv_output = torch.nn.ReLU()(conv_output)

    return conv_output


# Initialize the model
m = Model()

# Inputs to the model, randomly generated with values between 0 and 1:
x = np.random.rand(256, 3 * 7 * 7).astype('float32')

