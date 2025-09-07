
class TransformerModel(torch.nn.Module):
    def __init__(self, ntoken, ninp, nhead, nhid, dropout=0.5):
        super().__init__()
        self.encoder = torch.nn.Embedding(ntoken, ninp)  # Initialize the embedding layer for the source language
        self.pos_encoder = PositionalEncoding(ninp, dropout=dropout)  # Initialize the positional encoding layer with embedding size and dropout rate
        self.decoder = torch.nn.Linear(ninp, ntoken)  # Initialize the linear decoder layer that takes in the encoded output from the transformer model as input

        # Initialize the Transformer layers of the transformer model
        self.transformer_layers = torch.nn.TransformerEncoderLayer(d_model=ninp, nhead=nhead, dim_feedforward=nhid, dropout=dropout)
 
    def forward(self, src):  # Define the forward function that takes in the source language as input and outputs the predicted target language
        output = self.encoder(src) + self.pos_encoder(output)  # Encode the source sequence and add positional encoding

        for i in range(layers):
            layer_output = self.transformer_layer[i](output, src)  # Pass the encoded output through each transformer layer

        layer_output = self.decoder(layer_output[-1])  # Decode the last encoded output from each transformer layer
        return F.log_softmax(layer_output, dim=-1)


# Initializing the model with input size of 64 and embedding size of 256:
inputsize=64
embedding_dim = 256  # Set the embedding dimension to 256
 
m = TransformerModel(ntoken=len(TEXT.vocab), ninp=embedding_dim, nhead=10, nhid=128)

