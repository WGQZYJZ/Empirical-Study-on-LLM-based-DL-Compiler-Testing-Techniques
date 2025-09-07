
class ConvBNModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 48, (7, 5), padding=(0, 1))
        self.conv2 = torch.nn.Conv2d(48, 64, 9)
        self.conv3 = torch.nn.Conv2d(64, 96, 3)

        self.linear1 = torch.nn.Linear(7 * 7 * 96, 500)

    def forward(self, input):
       v1 = self.conv1(input)
       v2 = self.conv2(v1)
       v3 = self.conv3(v2)

       convbn_output = torch.nn.functional.batch_norm(
           v3,
           running_mean=None, 
           running_var=None, 
           training=False, # <- FUSE_CONV_BN will be triggered after this line
       )

# Initializing the model
m = ConvBNModel()

# Input tensor for the model
x1 = torch.randn(32, 3, 840)


