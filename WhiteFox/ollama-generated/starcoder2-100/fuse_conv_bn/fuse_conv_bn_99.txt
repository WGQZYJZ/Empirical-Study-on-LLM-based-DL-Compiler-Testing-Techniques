
class ConvModel(torch.nn.Module):
    def __init__(self, channel=2):
        super().__init__()
        
        self.conv1 = torch.nn.ConvNd(channel)
        self.conv2 = torch.nn.ConvNd(channel * 2)
        
    def forward(self, input_tensor):
__output__  = self.conv2(input_tensor)

 # Initializing the model and optimizer