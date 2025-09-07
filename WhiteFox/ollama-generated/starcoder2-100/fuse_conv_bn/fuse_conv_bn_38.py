
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv1d(256, 2048, kernel_size=3, stride=(2,), dilation=(1,))
        bn = torch.nn.BatchNorm1d(num_features=2048)
        output = bn(conv(x1))
        return output

# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(256, 3, 227).cuda() # Batch size 256 is randomly chosen (should be an integer multiple of 32)

