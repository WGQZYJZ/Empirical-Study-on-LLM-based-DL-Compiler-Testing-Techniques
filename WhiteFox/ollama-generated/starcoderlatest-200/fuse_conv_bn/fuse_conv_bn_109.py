 
class Model(torch.nn.Module):
    def __init__(self, in_chans, out_chans):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_chans, out_chans, 3)

    def forward(self, x):
        v1 = torch.nn.functional.conv2d(x, self.conv.weight)
        bn = torch.nn.functional.batch_norm(v1, (0,))
        return bn


# Initializing the model and input tensor
m = Model(in_chans=2, out_chans=3)
input_tensor = torch.randn(1, 2, 2, 2)

