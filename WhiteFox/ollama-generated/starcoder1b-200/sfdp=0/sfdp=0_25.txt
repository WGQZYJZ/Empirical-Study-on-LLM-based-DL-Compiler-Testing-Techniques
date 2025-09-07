
class Model(torch.nn.Module):
    def __init__(self, config: Config, train_data_config: TrainDataConfig):
        super().__init__()
        self.config = config
        self.train_data_config = train_data_config
        self.embedding  = torch.nn.Embedding(
            num_embeddings=train_data_config.vocab_size, 
            embedding_dim=config.hidden_size,
            padding_idx=0)

        # The input of the attention module is a query tensor. In this case, we compute a matrix multiplication between the embedding table and the hidden state vector `h` for each element in the batch.
        self.linear = torch.nn.Linear(config.hidden_size, config.hidden_size)
        self.attn = ScaledDotProductAttention(dim=1, dropout=config.attention_dropout)

        # The output of the attention module is an embedding tensor. In this case, we concatenate the query and key tensors into a single one to be concatenated with `output` by using broadcasting operation.
        self.linear2 = torch.nn.Linear(config.hidden_size, train_data_config.vocab_size)

        # The last layer of the Transformer network is fully-connected layer that receives `output`, computes a softmax on it and returns the output. We use negative log likelihood as the objective function because it is more general than cross-entropy loss.
        self.linear3 = torch.nn.Linear(config.hidden_size, 1)

    def forward(self, x: torch.Tensor):

        # Embedding the text with the trained word embedding table
        # Here we use broadcasting operation to concatenate the input and key tensors together.
        emb = self.embedding(x)
        # Add padding with zeros to fill in the blank tokens
        # For `src_seq` which is a B*T x H tensor,
        # it is also a T x 1 tensor because the hidden state is initialized with zeros.
        # This can be computed as:
        src_mask = torch.unsqueeze(torch.eq(x[:, :, 0], 0), dim=2)  # B*T x 1
        emb = torch.cat([emb, src_mask * 0], dim=2)

        # Compute a matrix of `output` between the embedding table and hidden state
        v = self.linear(emb)  # T x H
        # Multiply the output with a constant that multiplies each element in `input` by 1/sqrt(dim) (i.e., 1/sqrt(embedding_dim))
        scale = torch.rsqrt(torch.unsqueeze(torch.Tensor([self.config.hidden_size]), dim=0), dim=-1)

        # Use ScaledDotProductAttention to compute the attention weights for each element in the batch
        # To calculate `scaled_dot_product`, we need to compute a matrix of `query` times `key`.
        # Here we are using broadcasting operation to concatenate the input and key tensors together.
        q = self.linear2(emb).transpose(-2, -1)  # B*T x V
        k = torch.unsqueeze(q, dim=0).expand((self.config.batch_size, -1, -1))  # B*1 x V

        attention_weights = self.attn(query=q, key=k, value=v, scale=scale)

        # Use a fully-connected layer to concatenate the embedding tensor of the query and key tensors
        output = torch.cat([emb, k], dim=-1).view(-1, self.config.hidden_size)  # B*H

        # Apply a sigmoid function to compute a probability distribution over the possible vocabulary.
        # The probability of token `token` is equal to the value in row `token` in output.
        # We use negative log likelihood as the objective function because it is more general than cross-entropy loss.
        output = F.softmax(-self.linear3(output), dim=-1).log_softmax(-1)

        return output


# Initializing the model
m = Model(config, train_data_config)

