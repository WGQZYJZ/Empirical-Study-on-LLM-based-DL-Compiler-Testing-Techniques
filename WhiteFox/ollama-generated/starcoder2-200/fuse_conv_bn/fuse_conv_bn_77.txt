
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x0):
        v0 = x0 / 3.5
        t0  = torch.nn.functional.conv_transpose3d(v0, 4) # ConvTranspsoe3d: Applies a convolution that swaps the batch and the spatial dimensions.
        v1 = torch.nn.functional.batch_norm(t0) # BatchNorm: Layer which normalizes its input by adjusting and scaling the learned parameters for each feature dimension separately (one set of scale and bias per input channel).
        v2  = self.linear(v1)
        return v2


m = Model()

x0 = torch.randn(2, 48, 735394) / 3.5 # Normalize: Divide the input by a constant to scale the values. In this example, we normalize each channel independently across 1, 2 and 3 dimensions.
__output__  = m(x0)