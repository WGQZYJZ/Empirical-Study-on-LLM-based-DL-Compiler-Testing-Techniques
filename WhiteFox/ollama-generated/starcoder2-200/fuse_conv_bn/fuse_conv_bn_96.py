
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 80, kernel_size=5)
        
        self.conv2 = torch.nn.Conv2d(80, 96, kernel_size=4)

        self.conv3 = torch.nn.Conv2d(70, 120, kernel_size=3)
        

        self.batchnorm1 = torch.nn.BatchNorm2d(80)
        
        self.batchnorm2 = torch.nn.BatchNorm2d(96)
        
        self.batchnorm3 = torch.nn.BatchNorm2d(70)

        self.maxpooling = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        
        v1  = self.conv1(x)
        
        v1  = self.batchnorm1(v1)
        
        v2 = nn.Dropout(p=0.5)(v1)

        
        v3  = F.max_pool2d(v2 , kernel_size=(2, 2), stride=(2, 2), padding=(0, 0))
        v4 = self.conv2(v3)
        
        v4  = self.batchnorm2(v4)
        
        v5 = nn.Dropout(p=0.5)(v4)

        
        v6  = F.max_pool2d(v5 , kernel_size=(2, 2), stride=(1, 1), padding=(0, 0))
        v7 = self.conv3(v6)
        
        v8 = nn.Dropout(p=0.5)(v7)

        
        v9  = F.max_pool2d(v8 , kernel_size=(2, 2), stride=(1, 1), padding=(0, 0))
        v10 = self.maxpooling(v9)

        
        return torch.flatten(v10, 1).contiguous()


# Initializing the model:
model = Model()

# Inputs to the model
input_tensor=torch.randn(256, 3, 32, 32)
