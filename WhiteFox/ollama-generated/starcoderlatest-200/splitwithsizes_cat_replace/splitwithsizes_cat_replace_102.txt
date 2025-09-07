
class Model(torch.nn.Module):
    def __init__(self, input_shape=(32, 100)):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_shape[0], 8, 3)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return [v1]

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, *input_shape)
split_sizes = [x1.size()[i] for i in range(len(input_shape))]
