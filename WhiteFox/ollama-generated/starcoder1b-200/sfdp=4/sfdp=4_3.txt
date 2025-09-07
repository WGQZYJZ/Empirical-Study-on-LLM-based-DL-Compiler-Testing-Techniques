
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer1 = torch.nn.Linear(64, 32)
        self.linear_layer2 = torch.nn.Linear(32, 1)

    def forward(self, x1):
        batch_size, channel, height, width = x1.size()
        hidden_input = x1.view(batch_size, -1).clone().view(batch_size, -1, height * width)  # Flatten the input tensor to vector
        hidden_input = self.linear_layer1(hidden_input)
        hidden_input = self.relu(hidden_input)
        hidden_input = self.dropout_layer(hidden_input)
        output = self.linear_layer2(hidden_input).view(batch_size, channel, 1, 1) # Unflatten the vector to a (N, C, H, W) tensor
        return output


# Inputs to the model
x1 = torch.randn(3, 64, 64)
