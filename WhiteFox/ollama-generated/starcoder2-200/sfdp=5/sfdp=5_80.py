

class TransformerLayer(torch.nn.Module):
    def __init__(self, hidden_dim, ffn_hidden_dim, dropout=0.1):
        super().__init__()
        self.linear1 = torch.nn.Linear(hidden_dim, ffn_hidden_dim)  # Fully connected layer for the hidden dimension
        self.activation_func = torch.nn.GELU()  # GELU activation function from torch.nn.functional.gelu()
        self.dropout = torch.nn.Dropout(dropout)  # Dropout layer
        self.linear2 = torch.nn.Linear(ffn_hidden_dim, hidden_dim)  # Fully connected layer for the final dimension

  def forward(self, x):
    residual = x
    x = self.linear1(x)
    x = self.activation_func(x)
    x = self.dropout(x)
    x = self.linear2(x)
    return self.dropout(residual + x)


class TransformerEncoder(torch.nn.Module):
  def __init__(self, d_model=512, dropout=0.1):
      super().__init__()

      self.layer  = TransformerLayer(d_model, ffn_hidden_dim=4 * d_model, dropout=dropout)

  def forward(self, x):
    # batch_size: batch size of the inputs
    # embedding_dim: embedding dimension of the input
    # length: sequence length of the inputs 
    residual = x
    output  = self.layer(x)

    return output + residual

m  = TransformerEncoder()

