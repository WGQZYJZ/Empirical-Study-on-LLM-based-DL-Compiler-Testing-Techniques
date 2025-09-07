This pattern characterizes the Transformer encoder.


# Model
class Model(torch.nn.Module):
    def __init__(self, vocab_size):
        super().__init__()

        self.embedding = torch.nn.Embedding(vocab_size, 64)
        self.conv1 = torch.nn.Conv2d(64, 32, 5, stride=2)

        self.linear_qkv = torch.nn.Linear(128, 256)

        self.scale = torch.nn.Parameter(torch.ones([256]), requires_grad=False)

    def forward(self, x):
        batch_size, seq_len, embedding_dim = x.shape
        # Embedding layer:
        # [batch_size, seq_len, embedding_dim]
        embedded = self.embedding(x)  # [batch_size, seq_len, embedding_dim]

        # Convolutional Layer:
        # [batch_size, seq_len, input_channels * filter_height * filter_width]
        conv1 = F.leaky_relu(self.conv1(embedded), inplace=True)  # [batch_size, seq_len, output_channel]

        # Linear transformation from input size (256) to hidden size (128):
        # [batch_size, seq_len, output_channel]
        hidden = F.leaky_relu(self.linear_qkv(conv1))  # [batch_size, seq_len, output_channel]

        # Final Linear transformation from hidden size (128) to desired output size (vocab_size):
        # [batch_size, seq_len, vocab_size]
        linear = torch.matmul(hidden, self.scale.view([self.scale.shape[0], 1, -1]))

        return linear
softmax(QK^T @ K + softmax(QK^T @ V)) = softmax(QK^T @ K) / sqrt(N * hidden_size) * V
conv = torch.matmul(attn_weights @ value, self.scale)  # [batch_size, seq_len, embedding_dim]
