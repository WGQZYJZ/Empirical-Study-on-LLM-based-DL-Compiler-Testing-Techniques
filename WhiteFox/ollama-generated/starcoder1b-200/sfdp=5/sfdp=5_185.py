
class Model(torch.nn.Module):
    def __init__(self, embedding_dim: int = 512, num_heads: int = 8, depth: int = 12, dropout_p: float = 0.2):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_heads = num_heads
        self.depth = depth
        self.dropout_p = dropout_p
        
        self.layers = nn.ModuleList(
            [
                EncoderLayer(
                    num_attention_heads=num_heads, 
                    embedding_dim=embedding_dim, 
                    feedforward_dim=int(embedding_dim * 0.2),
                    dropout_p=dropout_p) for _ in range(depth)])
    
    def forward(self, x1: torch.Tensor):
        z = x1
        # Encode each input through the first TransformerLayer in the network.
        # Encode inputs through these layers for a full sequence. 
        # For example, input: [CLS], output: [[CLS]]
        
        layer_num = 0
        layer = self.layers[layer_num]
        z = layer(z)
        
        # Dropout on each TransformerLayer before outputting the final hidden states of the encoder.
        # During decoding time, we will be using these intermediate hidden states as initial inputs to the next decoder layers.
        for _ in range(self.depth - 1):
            z = torch.nn.functional.dropout(z, self.dropout_p)
        
        return z


# Initializing the model
m = Model()
x1 = torch.randn(1, 512, 64, 64)
