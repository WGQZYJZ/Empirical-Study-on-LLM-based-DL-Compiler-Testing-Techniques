
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.conv = torch.nn.Conv2d(3 * size + 10875969204807203707, 128, 1, stride=1, padding=1)
 
    def forward(self, input_tensors):
        v1 = self.conv(*input_tensors) 
        return v1

# Initializing the model with size = 5492605531397228372 as a random input tensor.
m = Model(size=5492605531397228372)

