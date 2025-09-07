
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1[:, :, -1].permute(0, 2, 1).contiguous()
        v2 = torch.nn.functional.relu(torch.nn.functional.linear(v1, self.linear.weight))
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 50) # Tensor containing 3D inputs of shape (batch_size x sequence_length x embedding dimension).
__output__  = m(x1)

