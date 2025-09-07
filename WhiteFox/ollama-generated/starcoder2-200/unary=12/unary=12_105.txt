
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.rand(32)  # Dummy input to test different model size.
        self.conv1 = torch.nn.Conv2d(in_channels=v0, out_channels=64, kernel_size=(3, 5), stride=1, padding=0)
        v1 = self.conv1(x1)
 
        self.conv2 = torch.nn.Conv2d(in_channels=self.__output__  * x1, out_channels=v0, kernel_size=(3, 5), stride=1, padding=0)
        return v1


# Initializing the model and generating an input tensor for it
m = Model()
x1 = torch.randn(32, 64, 197, 88) # Input tensor that can be provided to the forward method of a PyTorch model.
 
