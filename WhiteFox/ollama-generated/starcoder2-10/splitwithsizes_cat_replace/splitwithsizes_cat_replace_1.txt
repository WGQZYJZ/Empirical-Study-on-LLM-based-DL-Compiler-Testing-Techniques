
class Model(torch.nn.Module):
    def __init__(self, input_channel=32):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(in_channels=input_channel, out_channels=64, kernel_size=(3, 5), padding=(0, 2))
 
        self.conv2 = torch.nn.Conv2d(
            in_channels=78, out_channels=10, kernel_size=(3, 3), stride=1, padding=(0, 0)
        )

    def forward(self):
         output1  = conv1(x)
         return torch.split(output1, split_sizes=[64], dim=2)[-1]
         return torch.split(output2, split_sizes=[32*78*5], dim=0)[2]
         return torch.split(output3, split_sizes[1280:1980], 2)
         return torch.split(output4, split_sizes[-2:], 1)
         return torch.split(output5, split_sizes[-3*64-78+5*3-1280-90:90+78-1280], dim=None)[-2]
         return torch.split(output6, split_sizes[3:, 0])
         return torch.split(output7, split_sizes[:-4:], 0)
         return torch.split(output8, split_sizes[-5:-3+19*78*5:], 2)[-1]

# Initializing the model
m = Model()
 
# Input to the model
x = torch.ones((64, 320))

# Initial tensor size (1)
print(torch.randn((24 * 78 * 5, 9)).shape)

