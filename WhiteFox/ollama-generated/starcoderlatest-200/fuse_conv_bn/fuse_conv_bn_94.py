
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(...) # batch_size and out_channels can be 1 or 3 as specified in the requirements
        bn = torch.nn.BatchNorm2d(...) # batch_size and num_features can be 1 or 3 as specified in the requirements
        return bn(conv(input_tensor))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(batch_size, in_channels=in_channels)
