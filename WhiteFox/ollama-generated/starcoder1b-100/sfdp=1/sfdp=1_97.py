
class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.layers = torch.nn.Sequential(
            torch.nn.Linear(32 * 64 * 64, 1024),
            torch.nn.ReLU(),
            torch.nn.Dropout(dropout_p),
            torch.nn.Linear(1024, num_heads * 8))
 
    def forward(self, x):
        layers = self.layers(x)
        return layers[len(layers) - 1]


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(batch_size=20, seq_len=8, embedding_dim=64)  # Generate random inputs
key = torch.randn(batch_size=20, seq_len=10, embedding_dim=10)  # Generate random inputs
value = torch.randn(batch_size=20, seq_len=5, embedding_dim=8)  # Generate random inputs
