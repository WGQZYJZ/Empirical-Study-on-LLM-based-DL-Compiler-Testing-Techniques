

class MyModel(torch.nn.Module):
    def __init__(self, inchannel1, inchannel2) -> None:
        super().__init__()

        self.conv1 = torch.nn.Conv2d(inchannels=inchannel1, out_channels=outchannel1, kernel_size=(3, 3), stride=stride, padding=padding)
        self.relu1 = torch.nn.ReLU()
        
        self.conv2 = torch.nn.Conv2d(inchannels=inchannel1, inchannel2, kernel_size=(3, 3), stride=stride, padding=padding)
        self.add1 = torch.nn.Add()

    def forward(self, x):
        
        y1 = conv1(x)
        y1 = relu1(y1)
        
        y2 = conv2(y1)
        y = add1(x,y2)
        
        return y


# Initializing the model
model = Model(inchannel1, inchannel2)

# Input to the model 
input_tensor = torch.rand(inchannel1, outchannels1, 64, 64)
