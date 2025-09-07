
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 5, stride=2, padding=2)

    def forward(self, x1):
        v1  = self.conv1(x1)
        v2 = torch.softmax(v1, dim=-1).unsqueeze(-1)
        # Reshape query and key to a single dimension
        k = torch.reshape(v2, (-1, v1.shape[-1]))
        # Compute dot product (scaled_dot_product) using query and key vectors
        sdp  = self.conv2(torch.matmul(k, x1))
        v3 = sdp.max(-1)[0]  # Max along the batch axis of values to be retrieved
        return v3


# Initializing the model
m = Model()


