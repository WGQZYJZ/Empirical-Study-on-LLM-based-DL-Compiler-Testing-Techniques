

class FusedModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, kernel_size=7)

    def forward(self, input):
        conv1  = torch.nn.functional.conv2d(input, self.conv.weight, bias=None, stride=2, padding=3) # The Conv2d and BatchNorm2d are in evaluation mode 
        v1  = torch.nn.functional.relu(conv1)
        return torch.nn.functional.batch_norm(v1, running_mean=self.conv.running_mean, running_var=self.conv.running_var, momentum=0.1)

# Initializing the model
m = FusedModel()


Inputs to the model
x  = torch.randn(32, 3, 856, 480) # 856 x 480 is arbitrary size
