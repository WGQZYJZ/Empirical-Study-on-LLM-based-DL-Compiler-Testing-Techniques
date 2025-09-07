
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()

        self.embedding = nn.Embedding(config.vocab_size,
                                       config.embed_dim)  # Embedding layer to project a vocabulary to a fixed dimension

        # We can change this to nn.Linear() but it is recommended not to do so unless we know that the final output of the model will be in range [0, 1]
        self.linear = nn.Linear(config.embed_dim, config.hidden_dim)

        # No need to add an embedding layer after adding a linear layer since all layers have the same input size.
        self.layer_norm = nn.LayerNorm(config.hidden_dim)  # Layer normalization

        # The attention mechanism is computed on each output in order to compute the next set of weights. It is applied sequentially over different hidden states at every timestep and can be thought of as a stacked Transformer that concatenates inputs across time steps.
        self.dropout = nn.Dropout(config.attention_dropout)  # Apply dropout to the weighted attention outputs

        # The fully-connected layer computes the output of a single hidden unit by performing dot product with its weights, followed by a layer normalization operation on top. Note that since all layers have the same input size and output size, we can skip this linear layer in each case.
        self.linear_out = nn.Linear(config.hidden_dim, config.vocab_size)  # We need to pass in the hidden dimension because there are two outputs. The first output is the logits from a feed-forward network and the second output has been flattened so it is just the softmax of the weighted dot product across different time steps.

        self.init_weights()

    def forward(self, input):
        # Embedding layer to project vocabulary into the hidden dimension. This is exactly the same as the previous implementation, but without the embedding layer that would cause a problem with pre-trained models since they don't have the vocabulary embedded in their inputs (as we saw earlier).
        x = self.embedding(input)

        # We can change this to nn.Linear() but it is recommended not to do so unless we know that the final output of the model will be in range [0, 1]
        x = F.relu(self.linear(x))

        # Layer normalization before adding a dropout layer as done in previous layers. Note that since all layers have the same input size and output size, we can skip this operation for each case.
        x = self.layer_norm(x)
        x = self.dropout(x)  # Apply dropout to weighted attention outputs

        # We can change this to nn.Linear() but it is recommended not to do so unless we know that the final output of the model will be in range [0, 1]
        x = F.log_softmax(self.linear_out(x), dim=-1)
        return x

    def init_weights(self):
        nn.init.normal_(self.embedding.weight)  # Weight initialization: normal distribution initialized with std of 0.01, which matches the implementation of TensorFlow.
        nn.init.constant_(self.linear.bias, 0.)


# Initializing the model
model = Model(config=Config)

