
class Model(torch.nn.Module):
    def __init__(self, conv_size=2):
        super().__init__()

        self.conv1  = torch.nn.ConvXd(3, 6, kernel_size=[conv_size] * 4) # X can be 1, 2 or 3 representing the dimension
        self.conv2  = torch.nn.ConvXd(50, 80, kernel_size=4)
        self.conv3  = torch.nn.ConvXd(80, 768, kernel_size=[2] * 4)

        self.linear1   = torch.nn.Linear(3*3*768, 500) # Input tensor with more than two dimensions
        self.linear2   = torch.nn.Linear(100, 1000)
        self.conv_bn   = torch.nn.BatchNormXd(768)

        self.fc    = nn.Sequential(
            nn.Dropout(), 
            nn.Linear()
        )

    def forward(self, input):
        conv1  = self.conv2(self.conv3(self.conv1(input)))
        conv_bn   = torch.nn.functional.batch_norm(conv1)
        linear1  = self.linear1(conv1).permute([0], [2]).reshape(-1, 3*3*768) # Permute the 4th dimension
        linear2    = torch.nn.functional.linear(self.conv_bn(input))

        conv_out  = self.conv1(self.linear1)
        return (conv_out, conv_out, linear1, linear2, self.conv3(self.linear2(self.conv4)))

# Initializing the model
m  = Model()

# Inputs to the model
input  = torch.rand(10, 3, 768)

# Calling the forward() method of the model with the input tensor
__output__  = m(input)