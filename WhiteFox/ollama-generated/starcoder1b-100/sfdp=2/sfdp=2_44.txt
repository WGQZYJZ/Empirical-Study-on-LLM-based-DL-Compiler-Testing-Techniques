
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, 1)
        self.linear = torch.nn.Linear(8 * num_heads + 8, 256)

    def forward(self, x1):
        # Concatenate x1 along the first dimension to form a batch
        b = x1.shape[0]

        # Apply pointwise convolution with kernel size 1 to each element in x1 (batch_size, sequence_length, num_features)
        x1  = self.conv1d(x1)

        # Stack all the hidden states along the second dimension and project them back to a fixed number of hidden features by summing up over each hidden state
        v1 = torch.stack(torch.relu(self.linear(x1.view(-1, x1.shape[2]))), dim=1)
        return v1


# Initializing the model
m  = Model()

