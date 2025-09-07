
class Model(torch.nn.Module):
    def __init__(self, inchannel=3):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(inchannel, 64, kernel_size=(7, 7), padding=3)

        self.bn1 = torch.nn.BatchNorm2d(num_features=64)

    def forward(self, x):
        return torch.nn.functional.batch_norm(
            torch.nn.functional.conv2d(x, self.conv1.weight),
            self.bn1(x),
            self.conv1.bias
        )


m = Model()

 # Input to the model. 3x640x960x576, channel 3 
__x  = torch.zeros((3, 3, 640, 960), dtype=torch.float)

 # Initializing optimizer with default parameters. 
opt_config  = optimizer.Config()
opt = optimizer(m, opt_config)

 # Initialize a tensor to hold the optimized model
opt_model  = Model().cuda()

# Running forward pass for two epochs
for i in range(2):
  outs = m(__x)
    
# After forward pass, let's optimize the model with the optimizer. 
opt(m, __x);

 # Now, we will see the output after fusing the convolution layer and batch normalization layer
after_convbn = opt_model(x);