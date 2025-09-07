
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(16, 1)

    def forward(self, x):
        h = self.conv1(x)
        h = self.relu(h)

        # The output of the convolutions has shape (batch_size, num_heads * hidden_size, width, height)
        h = torch.flatten(h, 1)

        # Apply pointwise convolution with kernel size 1 to the output of the convolutions
        h = self.conv2(h)
        h = self.relu(h)

        h = torch.matmul(h, self.attn_mask)

        # Dropout with probability 0.3 and keep it at last layer
        h = F.dropout(h, p=0.3, training=self.training)

        # Compute the linear transformation on hidden space to get logits
        x = self.fc(h)
        return x


# Initializing the model
m = Model()


