
class Model(torch.nn.Module):
    def __init__(self, embed_dim=300, hid_dim=128, num_layers=2, dropout_p=0):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embed_dim) # Generate an embedding matrix based on the input vocabulary size and the embedding dimensionality
        self.embedding.weight.data.uniform_(-0.1, 0.1)
        self.fc = torch.nn.Linear(embed_dim, hid_dim * 4) 
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.pos_enc = torch.nn.Parameter(torch.randn(num_layers, hid_dim)) # Generate the positional encoding matrix
        self.layer_stack = torch.nn.ModuleList([self._make_layer() for _ in range(num_layers)]) # Initialize a stack of self-attention layers
 
    def forward(self, input_tensor):
        # Calculate the embedding matrix for the input tensor based on the vocabulary size and the input embedding dimensionality
        output = self.embedding(input_tensor) 
        
        # Calculate the positional encoding for the input
        output += self.pos_enc[:, :, input_tensor] 
        
        # Apply the layers to the output from the previous step
        output = [layer(output) for layer in self.layer_stack]
        
        # Reshape to generate an output tensor based on the previous layer outputs
        output = torch.cat(output, dim=-1)
        
        return self.dropout(output)
 
    def _make_layer(self):
        