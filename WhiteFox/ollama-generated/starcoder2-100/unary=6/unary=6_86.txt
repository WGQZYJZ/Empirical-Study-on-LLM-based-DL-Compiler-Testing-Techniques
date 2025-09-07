
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = torch.clamp_min(v1, 0)
        v3  = torch.clamp_max(v2, 6)
        v4  = v1 * v3 
        v5  = v4 / 6
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

# Test that model returns the same values as the original one in a simple case (with constant inputs/outputs).
input_tensor = np.random.rand(*((1,) + self._in_shape[0])).astype(np.float32) # (1, 3, 64, 64)
output       = np.squeeze(self.__output__(np.expand_dims(input_tensor, axis=0))) # ((64, 64))
assert np.allclose(output, self._in_shape[0]), "Your model is not correct!"

