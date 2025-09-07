
class Model(torch.nn.Module):
    def __init__(self, size_of_tensor_to_convolute=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(size_of_tensor_to_convolute, 16, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()

