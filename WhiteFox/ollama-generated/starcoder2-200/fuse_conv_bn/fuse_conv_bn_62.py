
class Model(torch.nn.Module):
    def __init__(self, channel: int=32):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(channel, 4 * channel, kernel_size=7, stride=2)

    def forward(self, x): 
        # Fused version of the conv and BN.
        output = torch.nn.functional.conv2d(x, weight=self.conv1.weight, bias=self.conv1.bias, stride=2, padding=(3, 3), groups=4)  
        output = torch.nn.functional.batch_norm(output, weight=self.conv1.running_mean, bias=self.conv1.running_var, momentum=0.9)
        return output

# Initializing the model
m = Model()

 # Inputs to the model 
x = torch.randn(2, 32, 56, 56)
__output__  = m(x)

