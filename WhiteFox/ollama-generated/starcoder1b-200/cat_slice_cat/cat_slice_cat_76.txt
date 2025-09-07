
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v = torch.cat([x[:, 0:9223372036854775807], x[:, :12]], dim=1) # Concatenate input tensors along dimension 1
        return torch.cat((x[:, 0:size], x[:, size:]), dim=1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
