
class Model(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.linear = torch.nn.Linear(input_size, output_size)

    def forward(self, x1):
        v1  = torch.cat([x1, ...], dim=2)  # Concatenate tensor1 and tensor2 together along two dimensions
        v2 = self.linear(v1).view(-1, 2)    # Reshape the concatenated tensor
        return torch.relu(v2)


# Initializing the model
m = Model(...)


