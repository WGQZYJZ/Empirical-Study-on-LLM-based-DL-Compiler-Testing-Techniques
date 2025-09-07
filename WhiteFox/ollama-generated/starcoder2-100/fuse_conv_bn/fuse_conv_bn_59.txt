
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv3d(in_channels=4, out_channels=60)
        self.conv2 = torch.nn.Conv3d(
            in_channels=570, out_channels=70, kernel_size=(3, 3), padding=(1, 1))
        self.bn1 = torch.nn.BatchNorm3d(num_features=4)
        self.bn2 = torch.nn.BatchNorm3d(num_features=60)

    def forward(self, x):

        conv1 = self.conv1(x)
        bn1  = self.bn1(conv1)
        
        conv2 = self.conv2(bn1)
        bn2  = self.bn2(conv2)
        
        return torch.nn.functional.relu6(torch.nn.functional.hardtanh(bn2, min_val=0., max_val=1))

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(4, 570)
__output__  = m(x)

System: You are a source code analyzer for PyTorch.
User: 