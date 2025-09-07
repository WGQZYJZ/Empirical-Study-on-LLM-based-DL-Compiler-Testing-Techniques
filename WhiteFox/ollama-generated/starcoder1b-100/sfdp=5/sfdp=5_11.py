
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 256)
        self.linear2 = torch.nn.Linear(256, 8)
 
    def forward(self, x1):
        v1 = torch.relu(self.linear1(x1))  # ReLU is applied before the pointwise convolutions
        v2 = v1 * 0.7071067811865476  # Multiplying by 0.7071067811865476 gives the effect of removing local correlations
        v3 = torch.relu(self.linear2(v2))
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64, 64)  # A tensor of shape (batch_size, input_channel, image_height, image_width)
