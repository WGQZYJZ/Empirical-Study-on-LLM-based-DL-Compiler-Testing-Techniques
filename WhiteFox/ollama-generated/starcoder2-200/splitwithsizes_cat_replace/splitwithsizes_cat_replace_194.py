

class Model(torch.nn.Module):
    def __init__(self, num_classes=2011):
        super().__init__()

        self.conv5 = torch.nn.Conv2d(
            384, 256, kernel_size=(7, 7), stride=(2, 2))

    def forward(self, input):
        # inputs to the model: 256x192
        v0 = self.conv5(input)

        # split/concat tensors, which will be used in this pattern.
        split_tensors = torch.split(v0, [384], dim=1)
        
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], 1)

        return True


# Initializing the model
m = Model()

# Input to the model is a 256x384x7x7 tensor.
inputs = torch.randn((batchsize, 384*7*7))
