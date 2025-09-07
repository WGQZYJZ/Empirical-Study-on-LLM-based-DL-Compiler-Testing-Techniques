
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        sdp = v1 * v1
        weights = sdp.softmax(-1)  # Compute attention weights using the softmax function.
        output = weights.matmul(v1)
        return output


# Initializing the model
m = Model()

