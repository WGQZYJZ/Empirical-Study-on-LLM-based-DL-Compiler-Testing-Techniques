
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(1, 8, 3, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = v1 * v3
        v5 = v4 / 6
        return v5


# Generating the test data for validating the output of the model
test_inputs_x1 = np.random.randn(1, 1, 28, 28).astype(np.float32)

# Expected outputs for the validation
__expected_outputs__ = torch.tensor([[[[7.4504e-02,  9.6730e+00,  5.7398e-01]]]])

