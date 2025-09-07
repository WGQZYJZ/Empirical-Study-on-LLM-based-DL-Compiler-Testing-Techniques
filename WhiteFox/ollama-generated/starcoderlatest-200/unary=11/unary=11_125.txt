
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = v3 / 6
        return v4


# Input tensors and expected output tensors
t1 = torch.randn(1, 8, 64, 64)
t2 = t1 + 3
t3 = torch.clamp(t2, min=0, max=6)
t4 = t3 / 6
__expected_output__ = t4


# Test code example
m = Model()
out = m(t1)
assert torch.allclose(out, __expected_output__, atol=1e-5, rtol=1e-5) == True
print('Test Passed.') # Please print out a string to indicate that the test passed.

